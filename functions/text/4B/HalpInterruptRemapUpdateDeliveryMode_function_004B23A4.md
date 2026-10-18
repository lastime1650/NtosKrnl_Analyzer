# HalpInterruptRemapUpdateDeliveryMode

- RVA: `0x004B23A4`–`0x004B23BE` (길이 `26` bytes)
- VA: `0x00000001404B23A4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpInterruptRemap](../54/HalpInterruptRemap_function_00542AE4.md) at `0x00542CAC`
- [HalpInterruptRemap](../54/HalpInterruptRemap_function_00542AE4.md) at `0x00542E3A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B23A4  81 79 04 D1 00 00 00            cmp dword ptr [rcx + 4], 0xd1
004B23AB  74 0F                           je 0x1404b23bc
004B23AD  8B 42 18                        mov eax, dword ptr [rdx + 0x18]
004B23B0  83 E8 05                        sub eax, 5
004B23B3  83 F8 01                        cmp eax, 1
004B23B6  77 04                           ja 0x1404b23bc
004B23B8  83 4A 0C 02                     or dword ptr [rdx + 0xc], 2
004B23BC  C3                              ret
004B23BD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpInterruptRemapUpdateDeliveryMode(__int64 a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned int *)(a1 + 4)) == 209) goto loc_004B23BC;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 24))) - (5));
    if (((unsigned int)(result)) <= 1) {
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpInterruptRemapUpdateDeliveryMode(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint32_t *)(arg1 + 0x4)) == 209) goto loc_004B23BC;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x18))) - (5));
    if (((uint32_t)(result)) <= 1) {
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg2` | `+ 0xC` | `32` | `R/W` |
| `Arg2` | `+ 0x18` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B23A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B23A4[BB_004B23A4]
  bb_004B23AD[BB_004B23AD]
  bb_004B23B8[BB_004B23B8]
  bb_004B23BC[BB_004B23BC]
  bb_004B23BD[BB_004B23BD]
  bb_004B23A4 -->|branch| bb_004B23BC
  bb_004B23A4 -->|fallthrough| bb_004B23AD
  bb_004B23AD -->|branch| bb_004B23BC
  bb_004B23AD -->|fallthrough| bb_004B23B8
  bb_004B23B8 -->|flow| bb_004B23BC
```
