# IopCloseIoCompletion

- RVA: `0x00A48E70`–`0x00A48E8E` (길이 `30` bytes)
- VA: `0x0000000140A48E70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A48E83` → [IopDeleteIoCompletionInternal](../../text/35/IopDeleteIoCompletionInternal_function_00351438.md) (function, `0x00351438`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A48E83` → [IopDeleteIoCompletionInternal](../../text/35/IopDeleteIoCompletionInternal_function_00351438.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A48E70  48 83 EC 28                     sub rsp, 0x28
00A48E74  48 8B C2                        mov rax, rdx
00A48E77  49 83 F9 01                     cmp r9, 1
00A48E7B  75 0B                           jne 0x140a48e88
00A48E7D  41 8A D1                        mov dl, r9b
00A48E80  48 8B C8                        mov rcx, rax
00A48E83  E8 B0 85 90 FF                  call 0x140351438
00A48E88  48 83 C4 28                     add rsp, 0x28
00A48E8C  C3                              ret
00A48E8D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopCloseIoCompletion(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = a2;
    if (a4 == 1) {
        a2 = (unsigned __int8)(a4);
        a1 = a2;
        result = IopDeleteIoCompletionInternal(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopCloseIoCompletion(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = Arg2;
    if (Arg4 == 1) {
        Arg2 = (uint8_t)(Arg4);
        Arg1 = Arg2;
        result = IopDeleteIoCompletionInternal(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A48E70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A48E70[BB_00A48E70]
  bb_00A48E7D[BB_00A48E7D]
  bb_00A48E88[BB_00A48E88]
  bb_00A48E8D[BB_00A48E8D]
  bb_00A48E70 -->|branch| bb_00A48E88
  bb_00A48E70 -->|fallthrough| bb_00A48E7D
  bb_00A48E7D -->|flow| bb_00A48E88
```
