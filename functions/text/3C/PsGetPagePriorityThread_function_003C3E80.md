# PsGetPagePriorityThread

- RVA: `0x003C3E80`–`0x003C3EAC` (길이 `44` bytes)
- VA: `0x00000001403C3E80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_002066BE](../20/Unknown_function_002066BE.md) at `0x0020673B`
- [PfLogFileDataAccess](../34/PfLogFileDataAccess_function_00342090.md) at `0x0034213C`
- [sub_003425E5](../34/Unknown_function_003425E5.md) at `0x00342601`
- [CcAsyncCopyRead](../35/CcAsyncCopyRead_function_00358880.md) at `0x00358A4E`
- [CcScheduleReadAheadNuma](../38/CcScheduleReadAheadNuma_function_0038883C.md) at `0x00388A9F`
- [EtwpTraceThreadRundown](EtwpTraceThreadRundown_function_003C370C.md) at `0x003C3819`
- [SmKmStoreHelperCommandProcess](SmKmStoreHelperCommandProcess_function_003C3AA4.md) at `0x003C3B3D`
- [SmKmStoreHelperCommandProcess](SmKmStoreHelperCommandProcess_function_003C3AA4.md) at `0x003C3B97`
- [CcInitializeCacheMapInternal](CcInitializeCacheMapInternal_function_003CC720.md) at `0x003CCD30`
- [CcCompleteAsyncRead](../45/CcCompleteAsyncRead_function_0045E7DC.md) at `0x0045E806`
- [CcPerformReadAhead](../48/CcPerformReadAhead_function_0048F738.md) at `0x0048FA53`
- [ExpWorkerThread](../4E/ExpWorkerThread_function_004ECAF0.md) at `0x004ED12A`
- [EtwTraceThread](../../page/90/EtwTraceThread_function_00905700.md) at `0x009057F1`
- [PfSnCheckActionsNeeded](../../page/95/PfSnCheckActionsNeeded_function_0095F538.md) at `0x0095F5BF`
- [PfSnAsyncContextInitialize](../../page/96/PfSnAsyncContextInitialize_function_00961168.md) at `0x009611E1`
- [NtQueryInformationThread](../../page/AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4278`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003C3E80  8B 81 A0 05 00 00               mov eax, dword ptr [rcx + 0x5a0]
003C3E86  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
003C3E8D  C1 E8 0C                        shr eax, 0xc
003C3E90  83 E0 07                        and eax, 7
003C3E93  48 8B 89 A0 02 00 00            mov rcx, qword ptr [rcx + 0x2a0]
003C3E9A  48 85 C9                        test rcx, rcx
003C3E9D  74 0B                           je 0x1403c3eaa
003C3E9F  8B 89 44 04 00 00               mov ecx, dword ptr [rcx + 0x444]
003C3EA5  3B C1                           cmp eax, ecx
003C3EA7  0F 43 C1                        cmovae eax, ecx
003C3EAA  C3                              ret
003C3EAB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsGetPagePriorityThread(__int64 a1)
{
    __int64 result;

    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 1440))) >> (12));
    result = (unsigned int)((result) & (7));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 672) != 0) {
        a1 = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 672) + 1092);
        if (((unsigned int)(result)) >= ((unsigned int)(a1))) { result = (unsigned int)(a1); }
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PsGetPagePriorityThread(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x5A0))) >> (12));
    result = (uint32_t)((result) & (7));
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x2A0) != 0) {
        Arg1 = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x2A0) + 0x444);
        if (((uint32_t)(result)) >= ((uint32_t)(Arg1))) { result = (uint32_t)(Arg1); }
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x220` | `64` | `R` |
| `Arg1` | `+ 0x5A0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003C3E80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003C3E80[BB_003C3E80]
  bb_003C3E9F[BB_003C3E9F]
  bb_003C3EAA[BB_003C3EAA]
  bb_003C3EAB[BB_003C3EAB]
  bb_003C3E80 -->|branch| bb_003C3EAA
  bb_003C3E80 -->|fallthrough| bb_003C3E9F
  bb_003C3E9F -->|flow| bb_003C3EAA
```
