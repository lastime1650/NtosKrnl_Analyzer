# Feature_SuspendThread2__private_IsEnabledNoReportingNoInline

- RVA: `0x005C357C`–`0x005C35AB` (길이 `47` bytes)
- VA: `0x00000001405C357C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005C35A0` → [Feature_SuspendThread2__private_IsEnabledFallback](Feature_SuspendThread2__private_IsEnabledFallback_function_005C3560.md) (function, `0x005C3560`)

### Direct callers
- [KiSuspendThread](../46/KiSuspendThread_function_0046B964.md) at `0x0046BC2B`
- [PspInsertThread](../../page/9F/PspInsertThread_function_009F0314.md) at `0x009F0880`
- [PsSuspendThread](../../page/A1/PsSuspendThread_function_00A110D0.md) at `0x00A110EB`
- [NtQueryInformationThread](../../page/AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE478E`
- [NtChangeThreadState](../../page/AE/NtChangeThreadState_function_00AEA210.md) at `0x00AEA276`
- [NtChangeThreadState](../../page/AE/NtChangeThreadState_function_00AEA210.md) at `0x00AEA285`
- [NtChangeThreadState](../../page/AE/NtChangeThreadState_function_00AEA210.md) at `0x00AEA2D4`
- [NtChangeThreadState](../../page/AE/NtChangeThreadState_function_00AEA210.md) at `0x00AEA2E2`

### Static image references
- `0x005C3586` → RVA `0x00FC48C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005C357C  48 83 EC 28                     sub rsp, 0x28
005C3580  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
005C3586  8B 05 34 13 A0 00               mov eax, dword ptr [rip + 0xa01334]
005C358C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005C3590  A8 02                           test al, 2
005C3592  74 05                           je 0x1405c3599
005C3594  83 E0 01                        and eax, 1
005C3597  EB 0C                           jmp 0x1405c35a5
005C3599  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
005C359E  33 D2                           xor edx, edx
005C35A0  E8 BB FF FF FF                  call 0x1405c3560
005C35A5  48 83 C4 28                     add rsp, 0x28
005C35A9  C3                              ret
005C35AA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_SuspendThread2__private_IsEnabledNoReportingNoInline(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10490676)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10490676)))) & (2)) == 0) goto loc_005C3599;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10490676))) & (1));
    goto loc_005C35A5;
loc_005C3599:
    a2 = 0;
    result = Feature_SuspendThread2__private_IsEnabledFallback(v_stack_p8, a2, a3, a4);
loc_005C35A5:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_SuspendThread2__private_IsEnabledNoReportingNoInline(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA01334)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA01334)))) & (2)) == 0) goto loc_005C3599;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA01334))) & (1));
    goto loc_005C35A5;
loc_005C3599:
    Arg2 = 0;
    result = Feature_SuspendThread2__private_IsEnabledFallback(v_stack_p8, Arg2, a3, a4);
loc_005C35A5:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005C357C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005C357C[BB_005C357C]
  bb_005C3594[BB_005C3594]
  bb_005C3599[BB_005C3599]
  bb_005C35A5[BB_005C35A5]
  bb_005C35AA[BB_005C35AA]
  bb_005C357C -->|branch| bb_005C3599
  bb_005C357C -->|fallthrough| bb_005C3594
  bb_005C3594 -->|branch| bb_005C35A5
  bb_005C3599 -->|flow| bb_005C35A5
```
