# PspLockJobExclusive

- RVA: `0x0091A4B8`–`0x0091A4DA` (길이 `34` bytes)
- VA: `0x000000014091A4B8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0091A4CF` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)

### Direct callers
- [PspConvertSiloToServerSilo](../77/PspConvertSiloToServerSilo_function_0077F9B4.md) at `0x0077FA9D`
- [PspQuitNextJobProcess](../78/PspQuitNextJobProcess_function_00785298.md) at `0x007852B8`
- [PspJobClose](PspJobClose_function_00916FE0.md) at `0x0091701B`
- [PspJobClose](PspJobClose_function_00916FE0.md) at `0x00917064`
- [PspEvaluateAndNotifyEmptyJob](PspEvaluateAndNotifyEmptyJob_function_00917D88.md) at `0x00917DB0`
- [PspGetNextJobProcess](PspGetNextJobProcess_function_00918450.md) at `0x00918478`
- [PspEnforceLimitsJobPostCallback](PspEnforceLimitsJobPostCallback_function_00919720.md) at `0x00919BA7`
- [NtQueryInformationJobObject](../9F/NtQueryInformationJobObject_function_009FB860.md) at `0x009FBCFE`
- [PspLockRootJobFromProcess](../A4/PspLockRootJobFromProcess_function_00A45BD8.md) at `0x00A45C13`
- [PspJobNotificationWorker](../A5/PspJobNotificationWorker_function_00A55CB0.md) at `0x00A55D7F`
- [PspNotificationPacketCallback](../A6/PspNotificationPacketCallback_function_00A67B30.md) at `0x00A67B51`
- [PspCreateSilo](../A8/PspCreateSilo_function_00A89CFC.md) at `0x00A89D4D`
- [sub_00B21AB8](../B2/Unknown_function_00B21AB8.md) at `0x00B21B6B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0091A4CF` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0091A4B8  48 83 EC 28                     sub rsp, 0x28
0091A4BC  48 85 D2                        test rdx, rdx
0091A4BF  74 08                           je 0x14091a4c9
0091A4C1  66 FF 8A E6 01 00 00            dec word ptr [rdx + 0x1e6]
0091A4C8  90                              nop
0091A4C9  48 83 C1 38                     add rcx, 0x38
0091A4CD  B2 01                           mov dl, 1
0091A4CF  E8 4C A9 8F FF                  call 0x140214e20
0091A4D4  48 83 C4 28                     add rsp, 0x28
0091A4D8  C3                              ret
0091A4D9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspLockJobExclusive(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 != 0) {
    }
    a1 = (a1) + (56);
    result = ExAcquireResourceExclusiveLite(a1, 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspLockJobExclusive(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 != 0) {
    }
    Arg1 = (Arg1) + (56);
    result = ExAcquireResourceExclusiveLite(Arg1, 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0091A4B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0091A4B8[BB_0091A4B8]
  bb_0091A4C1[BB_0091A4C1]
  bb_0091A4C9[BB_0091A4C9]
  bb_0091A4D9[BB_0091A4D9]
  bb_0091A4B8 -->|branch| bb_0091A4C9
  bb_0091A4B8 -->|fallthrough| bb_0091A4C1
  bb_0091A4C1 -->|flow| bb_0091A4C9
```
