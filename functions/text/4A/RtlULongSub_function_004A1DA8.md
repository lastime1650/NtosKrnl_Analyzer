# RtlULongSub

- RVA: `0x004A1DA8`–`0x004A1DC6` (길이 `30` bytes)
- VA: `0x00000001404A1DA8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [DbgkpTriageDumpSnapData](../58/DbgkpTriageDumpSnapData_function_005806E0.md) at `0x005807BE`
- [KiDeduplicateTriageDumpDataArrays](../5B/KiDeduplicateTriageDumpDataArrays_function_005B4748.md) at `0x005B4836`
- [KiDeduplicateTriageDumpDataArrays](../5B/KiDeduplicateTriageDumpDataArrays_function_005B4748.md) at `0x005B4845`
- [KiDeduplicateTriageDumpDataArrays](../5B/KiDeduplicateTriageDumpDataArrays_function_005B4748.md) at `0x005B490C`
- [BcpDisplayCriticalStringCentered](../69/BcpDisplayCriticalStringCentered_function_0069FAB8.md) at `0x0069FBCE`
- [RegRtlQueryKeyPathName](../../page/83/RegRtlQueryKeyPathName_function_00832AD8.md) at `0x00832BDB`
- [BiGetFilePathFromEfiPath](../../page/A9/BiGetFilePathFromEfiPath_function_00A90C1C.md) at `0x00A90D5A`
- [sub_00B34728](../../page/B3/Unknown_function_00B34728.md) at `0x00B3474E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A1DA8  3B CA                           cmp ecx, edx
004A1DAA  72 14                           jb 0x1404a1dc0
004A1DAC  44 8B C9                        mov r9d, ecx
004A1DAF  44 2B CA                        sub r9d, edx
004A1DB2  3B CA                           cmp ecx, edx
004A1DB4  45 89 08                        mov dword ptr [r8], r9d
004A1DB7  1B C0                           sbb eax, eax
004A1DB9  25 95 00 00 C0                  and eax, 0xc0000095
004A1DBE  C3                              ret
004A1DBF  CC                              int3
004A1DC0  41 83 C9 FF                     or r9d, 0xffffffff
004A1DC4  EB EC                           jmp 0x1404a1db2
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlULongSub(int a1, int a2, __int64 a3)
{
    __int64 result;

    if (a1 < a2) goto loc_004A1DC0;
    a4 = (unsigned int)(((unsigned int)(a1)) - (a2));
loc_004A1DB2:
    *(unsigned int *)(a3) = (unsigned int)(a4);
    result = (unsigned int)((result) & (0xC0000095ULL));
    return result;
loc_004A1DC0:
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
    goto loc_004A1DB2;
}
```

## 5. (Beta) C Style

```c
int64_t RtlULongSub(int32_t Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    if (Arg1 < Arg2) goto loc_004A1DC0;
    a4 = (uint32_t)(((uint32_t)(Arg1)) - (Arg2));
loc_004A1DB2:
    *(uint32_t *)(arg3) = (uint32_t)(a4);
    result = (uint32_t)((result) & (0xC0000095ULL));
    return result;
loc_004A1DC0:
    a4 = (uint32_t)((a4) | (0xFFFFFFFFULL));
    goto loc_004A1DB2;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A1DA8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A1DA8[BB_004A1DA8]
  bb_004A1DAC[BB_004A1DAC]
  bb_004A1DB2[BB_004A1DB2]
  bb_004A1DBF[BB_004A1DBF]
  bb_004A1DC0[BB_004A1DC0]
  bb_004A1DA8 -->|branch| bb_004A1DC0
  bb_004A1DA8 -->|fallthrough| bb_004A1DAC
  bb_004A1DAC -->|flow| bb_004A1DB2
  bb_004A1DBF -->|flow| bb_004A1DC0
  bb_004A1DC0 -->|branch| bb_004A1DB2
```
