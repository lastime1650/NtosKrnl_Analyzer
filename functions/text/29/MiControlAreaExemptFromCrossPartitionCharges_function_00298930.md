# MiControlAreaExemptFromCrossPartitionCharges

- RVA: `0x00298930`–`0x00298951` (길이 `33` bytes)
- VA: `0x0000000140298930`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiFlushRelease](MiFlushRelease_function_002982C0.md) at `0x00298443`
- [MiFlushRelease](MiFlushRelease_function_002982C0.md) at `0x00298522`
- [MiRemoveViewsFromSectionWithPfn](MiRemoveViewsFromSectionWithPfn_function_002986D4.md) at `0x0029876A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00298930  F6 41 3E 0C                     test byte ptr [rcx + 0x3e], 0xc
00298934  75 14                           jne 0x14029894a
00298936  48 83 79 40 00                  cmp qword ptr [rcx + 0x40], 0
0029893B  75 09                           jne 0x140298946
0029893D  0F B7 41 5E                     movzx eax, word ptr [rcx + 0x5e]
00298941  83 E0 01                        and eax, 1
00298944  C3                              ret
00298945  CC                              int3
00298946  33 C0                           xor eax, eax
00298948  C3                              ret
00298949  CC                              int3
0029894A  B8 01 00 00 00                  mov eax, 1
0029894F  C3                              ret
00298950  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiControlAreaExemptFromCrossPartitionCharges(__int64 a1)
{
    __int64 result;

    if (((*(unsigned __int8 *)(a1 + 62)) & (12)) != 0) goto loc_0029894A;
    if ((*(unsigned __int64 *)(a1 + 64)) != 0) goto loc_00298946;
    result = (unsigned int)((*(unsigned __int16 *)(a1 + 94)) & (1));
    return result;
loc_00298946:
    result = 0;
    return result;
loc_0029894A:
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t MiControlAreaExemptFromCrossPartitionCharges(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (((*(uint8_t *)(arg1 + 0x3E)) & (12)) != 0) goto loc_0029894A;
    if ((*(uint64_t *)(arg1 + 0x40)) != 0) goto loc_00298946;
    result = (uint32_t)((*(uint16_t *)(arg1 + 0x5E)) & (1));
    return result;
loc_00298946:
    result = 0;
    return result;
loc_0029894A:
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x3E` | `8` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x5E` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00298930&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00298930[BB_00298930]
  bb_00298936[BB_00298936]
  bb_0029893D[BB_0029893D]
  bb_00298945[BB_00298945]
  bb_00298946[BB_00298946]
  bb_00298949[BB_00298949]
  bb_0029894A[BB_0029894A]
  bb_00298950[BB_00298950]
  bb_00298930 -->|branch| bb_0029894A
  bb_00298930 -->|fallthrough| bb_00298936
  bb_00298936 -->|branch| bb_00298946
  bb_00298936 -->|fallthrough| bb_0029893D
  bb_00298945 -->|flow| bb_00298946
  bb_00298949 -->|flow| bb_0029894A
```
