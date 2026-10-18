# PopPowerRequestClose

- RVA: `0x00A9D500`–`0x00A9D518` (길이 `24` bytes)
- VA: `0x0000000140A9D500`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A9D50D` → [PopPowerRequestHandleClose](../../text/47/PopPowerRequestHandleClose_function_00477894.md) (function, `0x00477894`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A9D50D` → [PopPowerRequestHandleClose](../../text/47/PopPowerRequestHandleClose_function_00477894.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A9D500  48 83 EC 28                     sub rsp, 0x28
00A9D504  49 83 F9 01                     cmp r9, 1
00A9D508  75 08                           jne 0x140a9d512
00A9D50A  48 8B CA                        mov rcx, rdx
00A9D50D  E8 82 A3 9D FF                  call 0x140477894
00A9D512  48 83 C4 28                     add rsp, 0x28
00A9D516  C3                              ret
00A9D517  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerRequestClose(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a4 == 1) {
        a1 = a2;
        result = PopPowerRequestHandleClose(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPowerRequestClose(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg4 == 1) {
        Arg1 = Arg2;
        result = PopPowerRequestHandleClose(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A9D500&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A9D500[BB_00A9D500]
  bb_00A9D50A[BB_00A9D50A]
  bb_00A9D512[BB_00A9D512]
  bb_00A9D517[BB_00A9D517]
  bb_00A9D500 -->|branch| bb_00A9D512
  bb_00A9D500 -->|fallthrough| bb_00A9D50A
  bb_00A9D50A -->|flow| bb_00A9D512
```
