# KeInterlockedSetProcessorAffinityEx

- RVA: `0x00352560`–`0x003525BC` (길이 `92` bytes)
- VA: `0x0000000140352560`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `28`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiComputeGroupSchedulingRank](../21/KiComputeGroupSchedulingRank_function_0021EB84.md) at `0x0021ED14`
- [PpmParkReportParkedCore](../2D/PpmParkReportParkedCore_function_002D8488.md) at `0x002D8506`
- [PpmParkReportParkedCore](../2D/PpmParkReportParkedCore_function_002D8488.md) at `0x002D8535`
- [PpmParkReportParkedCore](../2D/PpmParkReportParkedCore_function_002D8488.md) at `0x002D85B9`
- [KiForceIdleParkUnparkProcessor](KiForceIdleParkUnparkProcessor_function_003523B8.md) at `0x003523F3`
- [PpmParkReportSoftParkChange](PpmParkReportSoftParkChange_function_003526DC.md) at `0x00352737`
- [PpmParkReportSoftParkChange](PpmParkReportSoftParkChange_function_003526DC.md) at `0x0035274B`
- [sub_00356086](Unknown_function_00356086.md) at `0x003561D5`
- [KiProcessNMI](../5B/KiProcessNMI_function_005B8950.md) at `0x005B89C2`
- [KeDeepSleepProcessor](../5B/KeDeepSleepProcessor_function_005BDB24.md) at `0x005BDB65`
- [KiStartIdleThread](../5C/KiStartIdleThread_function_005C46B0.md) at `0x005C473E`
- [PpmTestAndLockProcessor](../5D/PpmTestAndLockProcessor_function_005D08B4.md) at `0x005D09AF`
- [PpmParkReportForceParkChange](../5D/PpmParkReportForceParkChange_function_005DBE30.md) at `0x005DBEAC`
- [PpmParkReportForceParkChange](../5D/PpmParkReportForceParkChange_function_005DBE30.md) at `0x005DBEC7`
- [sub_006F962E](../6F/Unknown_function_006F962E.md) at `0x006F97DA`
- [sub_006F962E](../6F/Unknown_function_006F962E.md) at `0x006F97E7`

### Static image references
- `0x00352560` → RVA `0x00F231B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00352560  48 8B 05 49 0C BD 00            mov rax, qword ptr [rip + 0xbd0c49]
00352567  4C 8B C1                        mov r8, rcx
0035256A  8B D2                           mov edx, edx
0035256C  44 8B 14 90                     mov r10d, dword ptr [rax + rdx*4]
00352570  41 8B CA                        mov ecx, r10d
00352573  41 0F B7 40 02                  movzx eax, word ptr [r8 + 2]
00352578  C1 E9 06                        shr ecx, 6
0035257B  3B C1                           cmp eax, ecx
0035257D  76 39                           jbe 0x1403525b8
0035257F  41 83 E2 3F                     and r10d, 0x3f
00352583  8B D1                           mov edx, ecx
00352585  41 8A CA                        mov cl, r10b
00352588  41 B9 01 00 00 00               mov r9d, 1
0035258E  49 D3 E1                        shl r9, cl
00352591  41 0F 0D 4C D0 08               prefetchw byte ptr [r8 + rdx*8 + 8]
00352597  49 8B 44 D0 08                  mov rax, qword ptr [r8 + rdx*8 + 8]
0035259C  48 8B C8                        mov rcx, rax
0035259F  49 0B C9                        or rcx, r9
003525A2  F0 49 0F B1 4C D0 08            lock cmpxchg qword ptr [r8 + rdx*8 + 8], rcx
003525A9  75 F1                           jne 0x14035259c
003525AB  4C 85 C8                        test rax, r9
003525AE  B8 00 00 00 00                  mov eax, 0
003525B3  0F 95 C0                        setne al
003525B6  C3                              ret
003525B7  CC                              int3
003525B8  33 C0                           xor eax, eax
003525BA  C3                              ret
003525BB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeInterlockedSetProcessorAffinityEx(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;

    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12389449) + (unsigned int)(a2) * 4))))) >> (6));
    if (((unsigned int)(*(unsigned __int16 *)(a1 + 2))) <= ((unsigned int)(a1))) goto loc_003525B8;
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12389449) + (unsigned int)(a2) * 4))) & (63));
    a4 = (1) << ((unsigned __int8)((unsigned __int8)(v_r10)));
loc_0035259C:
    a1 = (*(unsigned __int64 *)(a1 + (unsigned int)((unsigned int)(a1)) * 8 + 8)) | (a4);
    if (condition_is_not_equal) goto loc_0035259C;
    result = (((*(unsigned __int64 *)(a1 + (unsigned int)((unsigned int)(a1)) * 8 + 8)) & (a4)) != 0) ? 1 : 0;
    return result;
loc_003525B8:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeInterlockedSetProcessorAffinityEx(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;

    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBD0C49) + (uint32_t)(Arg2) * 4))))) >> (6));
    if (((uint32_t)(*(uint16_t *)(arg1 + 0x2))) <= ((uint32_t)(Arg1))) goto loc_003525B8;
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBD0C49) + (uint32_t)(Arg2) * 4))) & (63));
    a4 = (1) << ((uint8_t)((uint8_t)(local_r10)));
loc_0035259C:
    Arg1 = (*(uint64_t *)(arg1 + (uint32_t)((uint32_t)(arg1)) * 8 + 0x8)) | (a4);
    if (condition_is_not_equal) goto loc_0035259C;
    result = (((*(uint64_t *)(arg1 + (uint32_t)((uint32_t)(arg1)) * 8 + 0x8)) & (a4)) != 0) ? 1 : 0;
    return result;
loc_003525B8:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x2` | `16` | `R` |
| `Arg1` | `+ 0x8 + rdx*8` | `8` | `R` |
| `Arg1` | `+ 0x8 + rdx*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00352560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00352560[BB_00352560]
  bb_0035257F[BB_0035257F]
  bb_0035259C[BB_0035259C]
  bb_003525AB[BB_003525AB]
  bb_003525B7[BB_003525B7]
  bb_003525B8[BB_003525B8]
  bb_003525BB[BB_003525BB]
  bb_00352560 -->|branch| bb_003525B8
  bb_00352560 -->|fallthrough| bb_0035257F
  bb_0035257F -->|flow| bb_0035259C
  bb_0035259C -->|branch| bb_0035259C
  bb_0035259C -->|fallthrough| bb_003525AB
  bb_003525B7 -->|flow| bb_003525B8
```
