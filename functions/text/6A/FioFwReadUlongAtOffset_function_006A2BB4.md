# FioFwReadUlongAtOffset

- RVA: `0x006A2BB4`–`0x006A2BDE` (길이 `42` bytes)
- VA: `0x00000001406A2BB4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006A2BC6` → [FioFwReadBytesAtOffset](../3E/FioFwReadBytesAtOffset_function_003E5948.md) (function, `0x003E5948`)

### Direct callers
- [RaspMapGlyphIndexToLocation](RaspMapGlyphIndexToLocation_function_006A29B4.md) at `0x006A2A51`
- [RaspMapGlyphIndexToLocation](RaspMapGlyphIndexToLocation_function_006A29B4.md) at `0x006A2A70`
- [BgpFoInitialize](../../init/C8/BgpFoInitialize_function_00C806B0.md) at `0x00C8073A`
- [BgpFoInitialize](../../init/C8/BgpFoInitialize_function_00C806B0.md) at `0x00C80760`
- [BgpFoInitialize](../../init/C8/BgpFoInitialize_function_00C806B0.md) at `0x00C807A5`
- [FopInitializeFonts](../../init/C8/FopInitializeFonts_function_00C808FC.md) at `0x00C80979`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006A2BB4  40 53                           push rbx
006A2BB6  48 83 EC 20                     sub rsp, 0x20
006A2BBA  49 8B D8                        mov rbx, r8
006A2BBD  4D 8B C8                        mov r9, r8
006A2BC0  41 B8 04 00 00 00               mov r8d, 4
006A2BC6  E8 7D 2D D4 FF                  call 0x1403e5948
006A2BCB  85 C0                           test eax, eax
006A2BCD  78 08                           js 0x1406a2bd7
006A2BCF  8B 03                           mov eax, dword ptr [rbx]
006A2BD1  0F C8                           bswap eax
006A2BD3  89 03                           mov dword ptr [rbx], eax
006A2BD5  33 C0                           xor eax, eax
006A2BD7  48 83 C4 20                     add rsp, 0x20
006A2BDB  5B                              pop rbx
006A2BDC  C3                              ret
006A2BDD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FioFwReadUlongAtOffset(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = FioFwReadBytesAtOffset(a1, a2, 4, a3);
    if (!(sign_flag)) {
        result = *(unsigned int *)(a3);
        *(unsigned int *)(a3) = (unsigned int)(result);
        result = 0;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FioFwReadUlongAtOffset(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = FioFwReadBytesAtOffset(Arg1, Arg2, 4, Arg3);
    if (!(sign_flag)) {
        result = *(uint32_t *)(arg3);
        *(uint32_t *)(arg3) = (uint32_t)(result);
        result = 0;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006A2BB4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006A2BB4[BB_006A2BB4]
  bb_006A2BCF[BB_006A2BCF]
  bb_006A2BD7[BB_006A2BD7]
  bb_006A2BDD[BB_006A2BDD]
  bb_006A2BB4 -->|branch| bb_006A2BD7
  bb_006A2BB4 -->|fallthrough| bb_006A2BCF
  bb_006A2BCF -->|flow| bb_006A2BD7
```
