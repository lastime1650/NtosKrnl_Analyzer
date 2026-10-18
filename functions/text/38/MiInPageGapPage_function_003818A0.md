# MiInPageGapPage

- RVA: `0x003818A0`–`0x003818BF` (길이 `31` bytes)
- VA: `0x00000001403818A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiFinishHardFault](../2B/MiFinishHardFault_function_002B6F10.md) at `0x002B7595`
- [sub_0038167C](Unknown_function_0038167C.md) at `0x003816B3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003818A0  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
003818A3  C1 E8 10                        shr eax, 0x10
003818A6  24 07                           and al, 7
003818A8  3C 07                           cmp al, 7
003818AA  74 04                           je 0x1403818b0
003818AC  33 C0                           xor eax, eax
003818AE  C3                              ret
003818AF  CC                              int3
003818B0  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
003818B4  33 C0                           xor eax, eax
003818B6  48 83 F9 FD                     cmp rcx, -3
003818BA  0F 94 C0                        sete al
003818BD  C3                              ret
003818BE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInPageGapPage(__int64 a1)
{
    __int64 result;

    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned __int8)((result) & (7));
    if (((unsigned __int8)(result)) == 7) goto loc_003818B0;
    result = 0;
    return result;
loc_003818B0:
    result = 0;
    result = ((*(unsigned __int64 *)(a1 + 8)) == -3) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiInPageGapPage(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint8_t)((result) & (7));
    if (((uint8_t)(result)) == 7) goto loc_003818B0;
    result = 0;
    return result;
loc_003818B0:
    result = 0;
    result = ((*(uint64_t *)(arg1 + 0x8)) == -3) ? 1 : 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003818A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003818A0[BB_003818A0]
  bb_003818AC[BB_003818AC]
  bb_003818AF[BB_003818AF]
  bb_003818B0[BB_003818B0]
  bb_003818BE[BB_003818BE]
  bb_003818A0 -->|branch| bb_003818B0
  bb_003818A0 -->|fallthrough| bb_003818AC
  bb_003818AF -->|flow| bb_003818B0
```
