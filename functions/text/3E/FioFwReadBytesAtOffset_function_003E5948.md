# FioFwReadBytesAtOffset

- RVA: `0x003E5948`–`0x003E5974` (길이 `44` bytes)
- VA: `0x00000001403E5948`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `15`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003E5960` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [RaspInitializeGlyphData](RaspInitializeGlyphData_function_003E54B8.md) at `0x003E5743`
- [RaspInitializeGlyphData](RaspInitializeGlyphData_function_003E54B8.md) at `0x003E5798`
- [RaspInitializeGlyphData](RaspInitializeGlyphData_function_003E54B8.md) at `0x003E583B`
- [RaspInitializeGlyphData](RaspInitializeGlyphData_function_003E54B8.md) at `0x003E58C5`
- [FioFwReadUshortAtOffset](../4F/FioFwReadUshortAtOffset_function_004F98A0.md) at `0x004F98B2`
- [RaspInitializeCompositeGlyphData](../6A/RaspInitializeCompositeGlyphData_function_006A2138.md) at `0x006A222F`
- [RaspLoadBearings](../6A/RaspLoadBearings_function_006A24A8.md) at `0x006A24F3`
- [RaspLoadBearings](../6A/RaspLoadBearings_function_006A24A8.md) at `0x006A2533`
- [RaspLoadBearings](../6A/RaspLoadBearings_function_006A24A8.md) at `0x006A2556`
- [FioFwReadUlongAtOffset](../6A/FioFwReadUlongAtOffset_function_006A2BB4.md) at `0x006A2BC6`
- [FopGetTableOffsetAndSize](../../init/C8/FopGetTableOffsetAndSize_function_00C807F8.md) at `0x00C8083A`
- [FopGetTableOffsetAndSize](../../init/C8/FopGetTableOffsetAndSize_function_00C807F8.md) at `0x00C80881`
- [FopReadCmapTable](../../init/C8/FopReadCmapTable_function_00C80A54.md) at `0x00C80A94`
- [FopReadCmapTable](../../init/C8/FopReadCmapTable_function_00C80A54.md) at `0x00C80B30`
- [FopReadMappingTable](../../init/C8/FopReadMappingTable_function_00C80BA4.md) at `0x00C80C40`
- [FopReadMappingTable](../../init/C8/FopReadMappingTable_function_00C80BA4.md) at `0x00C80CE1`
- [FopReadNamingTable](../../init/C8/FopReadNamingTable_function_00C80D90.md) at `0x00C80DD4`
- [FopReadNamingTable](../../init/C8/FopReadNamingTable_function_00C80D90.md) at `0x00C80E79`
- [FopValidateFontNameTable](../../init/C8/FopValidateFontNameTable_function_00C80F14.md) at `0x00C81003`
- [BgpRasInitializeRasterizer](../../init/C8/BgpRasInitializeRasterizer_function_00C81A2C.md) at `0x00C81B36`
- [BgpRasInitializeRasterizer](../../init/C8/BgpRasInitializeRasterizer_function_00C81A2C.md) at `0x00C81B98`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E5948  48 83 EC 28                     sub rsp, 0x28
003E594C  42 8D 04 02                     lea eax, [rdx + r8]
003E5950  3B 41 08                        cmp eax, dword ptr [rcx + 8]
003E5953  77 18                           ja 0x1403e596d
003E5955  8B D2                           mov edx, edx
003E5957  48 03 11                        add rdx, qword ptr [rcx]
003E595A  49 8B C9                        mov rcx, r9
003E595D  45 8B C0                        mov r8d, r8d
003E5960  E8 DB 0E 2E 00                  call 0x1406c6840
003E5965  33 C0                           xor eax, eax
003E5967  48 83 C4 28                     add rsp, 0x28
003E596B  C3                              ret
003E596C  CC                              int3
003E596D  B8 0D 00 00 C0                  mov eax, 0xc000000d
003E5972  EB F3                           jmp 0x1403e5967
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FioFwReadBytesAtOffset(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((unsigned int)(a2 + a3 * 1)) > (*(unsigned int *)(a1 + 8))) goto loc_003E596D;
    a2 = ((unsigned int)((unsigned int)(a2))) + (*(unsigned __int64 *)(a1));
    result = memcpy(a4, a2, (unsigned int)((unsigned int)(a3)), a4);
    result = 0;
loc_003E5967:
    v_rsp = (v_rsp) + (40);
    return result;
loc_003E596D:
    goto loc_003E5967;
}
```

## 5. (Beta) C Style

```c
int64_t FioFwReadBytesAtOffset(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((uint32_t)(Arg2 + Arg3 * 1)) > (*(uint32_t *)(arg1 + 0x8))) goto loc_003E596D;
    Arg2 = ((uint32_t)((uint32_t)(Arg2))) + (*(uint64_t *)(arg1));
    result = memcpy(Arg4, Arg2, (uint32_t)((uint32_t)(Arg3)), Arg4);
    result = 0;
loc_003E5967:
    local_rsp = (local_rsp) + (40);
    return result;
loc_003E596D:
    goto loc_003E5967;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg2` | `+ 0x0 + r8*1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E5948&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003E5948[BB_003E5948]
  bb_003E5955[BB_003E5955]
  bb_003E5967[BB_003E5967]
  bb_003E596C[BB_003E596C]
  bb_003E596D[BB_003E596D]
  bb_003E5948 -->|branch| bb_003E596D
  bb_003E5948 -->|fallthrough| bb_003E5955
  bb_003E5955 -->|flow| bb_003E5967
  bb_003E596C -->|flow| bb_003E596D
  bb_003E596D -->|branch| bb_003E5967
```
