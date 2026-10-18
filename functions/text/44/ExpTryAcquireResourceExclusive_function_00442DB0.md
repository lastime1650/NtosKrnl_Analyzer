# ExpTryAcquireResourceExclusive

- RVA: `0x00442DB0`–`0x00442DD1` (길이 `33` bytes)
- VA: `0x0000000140442DB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ExpTryToAcquireResourceExclusiveLite](../65/ExpTryToAcquireResourceExclusiveLite_function_00658FEC.md) at `0x00659052`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00442DB0  83 79 40 00                     cmp dword ptr [rcx + 0x40], 0
00442DB4  75 17                           jne 0x140442dcd
00442DB6  B8 80 00 00 00                  mov eax, 0x80
00442DBB  66 09 41 1A                     or word ptr [rcx + 0x1a], ax
00442DBF  B8 01 00 00 00                  mov eax, 1
00442DC4  66 89 41 18                     mov word ptr [rcx + 0x18], ax
00442DC8  89 41 40                        mov dword ptr [rcx + 0x40], eax
00442DCB  C3                              ret
00442DCC  CC                              int3
00442DCD  32 C0                           xor al, al
00442DCF  C3                              ret
00442DD0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpTryAcquireResourceExclusive(__int64 a1)
{
    __int64 result;

    if ((*(unsigned int *)(a1 + 64)) != 0) goto loc_00442DCD;
    *(unsigned __int16 *)(a1 + 24) = 1;
    *(unsigned int *)(a1 + 64) = 1;
    return 1;
loc_00442DCD:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpTryAcquireResourceExclusive(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((*(uint32_t *)(arg1 + 0x40)) != 0) goto loc_00442DCD;
    *(uint16_t *)(arg1 + 0x18) = 1;
    *(uint32_t *)(arg1 + 0x40) = 1;
    return 1;
loc_00442DCD:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `16` | `W` |
| `Arg1` | `+ 0x1A` | `16` | `R/W` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x40` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00442DB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00442DB0[BB_00442DB0]
  bb_00442DB6[BB_00442DB6]
  bb_00442DCC[BB_00442DCC]
  bb_00442DCD[BB_00442DCD]
  bb_00442DD0[BB_00442DD0]
  bb_00442DB0 -->|branch| bb_00442DCD
  bb_00442DB0 -->|fallthrough| bb_00442DB6
  bb_00442DCC -->|flow| bb_00442DCD
```
