# PsTerminateSystemThread

- RVA: `0x009BCE50`–`0x009BCE7D` (길이 `45` bytes)
- VA: `0x00000001409BCE50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F758`
- 디코드: `12`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009BCE76` → [PspTerminateThreadByPointer](../90/PspTerminateThreadByPointer_function_00905E80.md) (function, `0x00905E80`)

### Direct callers
- [PopIrpWorker](../../text/26/PopIrpWorker_function_0026D410.md) at `0x0026D73B`
- [InbvRotateGuiBootDisplay](../../text/59/InbvRotateGuiBootDisplay_function_00590680.md) at `0x005906CC`
- [DifPsTerminateSystemThreadWrapper](../../text/63/DifPsTerminateSystemThreadWrapper_function_0063B0A0.md) at `0x0063B163`
- [ExpExpirationThread](../7C/ExpExpirationThread_function_007C5AF0.md) at `0x007C5B1F`
- [CmpLoadHiveThread](../7D/CmpLoadHiveThread_function_007DB040.md) at `0x007DB405`
- [CmpHiveCachePopulateHiveEntryThread](../7F/CmpHiveCachePopulateHiveEntryThread_function_007F5FD0.md) at `0x007F63B8`
- [IopThreadStart](IopThreadStart_function_009BCDF0.md) at `0x009BCE33`
- [EtwpLogger](EtwpLogger_function_009BE310.md) at `0x009BE759`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009BCE50  48 83 EC 28                     sub rsp, 0x28
009BCE54  8B D1                           mov edx, ecx
009BCE56  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009BCE5F  F7 41 74 00 04 00 00            test dword ptr [rcx + 0x74], 0x400
009BCE66  75 0B                           jne 0x1409bce73
009BCE68  B8 0D 00 00 C0                  mov eax, 0xc000000d
009BCE6D  48 83 C4 28                     add rsp, 0x28
009BCE71  C3                              ret
009BCE72  CC                              int3
009BCE73  41 B0 01                        mov r8b, 1
009BCE76  E8 05 90 F4 FF                  call 0x140905e80
009BCE7B  EB F0                           jmp 0x1409bce6d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsTerminateSystemThread(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 116)) & (0x400ULL)) != 0) goto loc_009BCE73;
loc_009BCE6D:
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(0xC000000DULL);
loc_009BCE73:
    result = PspTerminateThreadByPointer(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(a1), 1, a4);
    goto loc_009BCE6D;
}
```

## 5. (Beta) C Style

```c
int64_t PsTerminateSystemThread(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x74)) & (0x400ULL)) != 0) goto loc_009BCE73;
loc_009BCE6D:
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(0xC000000DULL);
loc_009BCE73:
    result = PspTerminateThreadByPointer(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(Arg1), 1, a4);
    goto loc_009BCE6D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009BCE50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009BCE50[BB_009BCE50]
  bb_009BCE68[BB_009BCE68]
  bb_009BCE6D[BB_009BCE6D]
  bb_009BCE72[BB_009BCE72]
  bb_009BCE73[BB_009BCE73]
  bb_009BCE50 -->|branch| bb_009BCE73
  bb_009BCE50 -->|fallthrough| bb_009BCE68
  bb_009BCE68 -->|flow| bb_009BCE6D
  bb_009BCE72 -->|flow| bb_009BCE73
  bb_009BCE73 -->|branch| bb_009BCE6D
```
