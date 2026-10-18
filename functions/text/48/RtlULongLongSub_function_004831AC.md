# RtlULongLongSub

- RVA: `0x004831AC`–`0x004831CC` (길이 `32` bytes)
- VA: `0x00000001404831AC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiAdjustTimer2DueTimes](../3A/KiAdjustTimer2DueTimes_function_003A3550.md) at `0x003A375B`
- [IopAddCodeRegion](../59/IopAddCodeRegion_function_005941B4.md) at `0x0059432C`
- [IopFillTriageDumpDataBlocks](../59/IopFillTriageDumpDataBlocks_function_005953E8.md) at `0x005954A9`
- [sub_006E635E](../6E/Unknown_function_006E635E.md) at `0x006E6373`
- [AslpFileGetCrcChecksum](../../page/81/AslpFileGetCrcChecksum_function_0081E6DC.md) at `0x0081E754`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004831AC  48 3B CA                        cmp rcx, rdx
004831AF  72 15                           jb 0x1404831c6
004831B1  4C 8B C9                        mov r9, rcx
004831B4  4C 2B CA                        sub r9, rdx
004831B7  48 3B CA                        cmp rcx, rdx
004831BA  4D 89 08                        mov qword ptr [r8], r9
004831BD  1B C0                           sbb eax, eax
004831BF  25 95 00 00 C0                  and eax, 0xc0000095
004831C4  C3                              ret
004831C5  CC                              int3
004831C6  49 83 C9 FF                     or r9, 0xffffffffffffffff
004831CA  EB EB                           jmp 0x1404831b7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlULongLongSub(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    if (a1 < a2) goto loc_004831C6;
    a4 = (a1) - (a2);
loc_004831B7:
    *(unsigned __int64 *)(a3) = a4;
    result = (unsigned int)((result) & (0xC0000095ULL));
    return result;
loc_004831C6:
    a4 = (a4) | (-1);
    goto loc_004831B7;
}
```

## 5. (Beta) C Style

```c
int64_t RtlULongLongSub(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    if (Arg1 < Arg2) goto loc_004831C6;
    a4 = (Arg1) - (Arg2);
loc_004831B7:
    *(uint64_t *)(arg3) = a4;
    result = (uint32_t)((result) & (0xC0000095ULL));
    return result;
loc_004831C6:
    a4 = (a4) | (-1);
    goto loc_004831B7;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004831AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004831AC[BB_004831AC]
  bb_004831B1[BB_004831B1]
  bb_004831B7[BB_004831B7]
  bb_004831C5[BB_004831C5]
  bb_004831C6[BB_004831C6]
  bb_004831AC -->|branch| bb_004831C6
  bb_004831AC -->|fallthrough| bb_004831B1
  bb_004831B1 -->|flow| bb_004831B7
  bb_004831C5 -->|flow| bb_004831C6
  bb_004831C6 -->|branch| bb_004831B7
```
