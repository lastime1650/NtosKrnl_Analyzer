# ExpCloseWorkerFactory

- RVA: `0x00A6C4C0`–`0x00A6C4D8` (길이 `24` bytes)
- VA: `0x0000000140A6C4C0`
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
- `0x00A6C4CD` → [ExpShutdownWorkerFactory](../../text/2A/ExpShutdownWorkerFactory_function_002A4F70.md) (function, `0x002A4F70`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A6C4CD` → [ExpShutdownWorkerFactory](../../text/2A/ExpShutdownWorkerFactory_function_002A4F70.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A6C4C0  48 83 EC 28                     sub rsp, 0x28
00A6C4C4  49 83 F9 01                     cmp r9, 1
00A6C4C8  75 08                           jne 0x140a6c4d2
00A6C4CA  48 8B CA                        mov rcx, rdx
00A6C4CD  E8 9E 8A 83 FF                  call 0x1402a4f70
00A6C4D2  48 83 C4 28                     add rsp, 0x28
00A6C4D6  C3                              ret
00A6C4D7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpCloseWorkerFactory(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a4 == 1) {
        a1 = a2;
        result = ExpShutdownWorkerFactory(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpCloseWorkerFactory(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg4 == 1) {
        Arg1 = Arg2;
        result = ExpShutdownWorkerFactory(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A6C4C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A6C4C0[BB_00A6C4C0]
  bb_00A6C4CA[BB_00A6C4CA]
  bb_00A6C4D2[BB_00A6C4D2]
  bb_00A6C4D7[BB_00A6C4D7]
  bb_00A6C4C0 -->|branch| bb_00A6C4D2
  bb_00A6C4C0 -->|fallthrough| bb_00A6C4CA
  bb_00A6C4CA -->|flow| bb_00A6C4D2
```
