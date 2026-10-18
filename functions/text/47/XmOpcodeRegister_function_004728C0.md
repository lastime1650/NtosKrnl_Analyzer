# XmOpcodeRegister

- RVA: `0x004728C0`–`0x00472903` (길이 `67` bytes)
- VA: `0x00000001404728C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `20`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004728EC` → [XmSetSourceValue](XmSetSourceValue_function_004737A8.md) (function, `0x004737A8`)
- `0x004728FC` → [XmSetDestinationValue](XmSetDestinationValue_function_004734EC.md) (function, `0x004734EC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004728C0  48 83 EC 28                     sub rsp, 0x28
004728C4  44 8B 41 70                     mov r8d, dword ptr [rcx + 0x70]
004728C8  8A 81 8A 00 00 00               mov al, byte ptr [rcx + 0x8a]
004728CE  F6 D8                           neg al
004728D0  1B D2                           sbb edx, edx
004728D2  41 83 E0 07                     and r8d, 7
004728D6  83 E2 02                        and edx, 2
004728D9  FF C2                           inc edx
004728DB  89 51 78                        mov dword ptr [rcx + 0x78], edx
004728DE  48 8D 51 18                     lea rdx, [rcx + 0x18]
004728E2  83 79 7C 24                     cmp dword ptr [rcx + 0x7c], 0x24
004728E6  4A 8D 14 82                     lea rdx, [rdx + r8*4]
004728EA  75 10                           jne 0x1404728fc
004728EC  E8 B7 0E 00 00                  call 0x1404737a8
004728F1  B8 01 00 00 00                  mov eax, 1
004728F6  48 83 C4 28                     add rsp, 0x28
004728FA  C3                              ret
004728FB  CC                              int3
004728FC  E8 EB 0B 00 00                  call 0x1404734ec
00472901  EB EE                           jmp 0x1404728f1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall XmOpcodeRegister(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned __int8)(-(*(unsigned __int8 *)(a1 + 138)));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 112))) & (7));
    a2 = (unsigned int)((a2) & (2));
    a2 = (unsigned int)((a2) + 1);
    *(unsigned int *)(a1 + 120) = a2;
    if ((*(unsigned int *)(a1 + 124)) != 36) goto loc_004728FC;
    result = XmSetSourceValue(a1, a1 + 24 + a3 * 4, a3, a4);
loc_004728F1:
    v_rsp = (v_rsp) + (40);
    return 1;
loc_004728FC:
    result = XmSetDestinationValue(a1, a1 + 24 + a3 * 4, a3, a4);
    goto loc_004728F1;
}
```

## 5. (Beta) C Style

```c
int64_t XmOpcodeRegister(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint8_t)(-(*(uint8_t *)(arg1 + 0x8A)));
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x70))) & (7));
    Arg2 = (uint32_t)((Arg2) & (2));
    Arg2 = (uint32_t)((Arg2) + 1);
    *(uint32_t *)(arg1 + 0x78) = Arg2;
    if ((*(uint32_t *)(arg1 + 0x7C)) != 36) goto loc_004728FC;
    result = XmSetSourceValue(Arg1, Arg1 + 24 + a3 * 4, a3, a4);
loc_004728F1:
    local_rsp = (local_rsp) + (40);
    return 1;
loc_004728FC:
    result = XmSetDestinationValue(Arg1, Arg1 + 24 + a3 * 4, a3, a4);
    goto loc_004728F1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + r8*4` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x78` | `32` | `W` |
| `Arg1` | `+ 0x7C` | `32` | `R` |
| `Arg1` | `+ 0x8A` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004728C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004728C0[BB_004728C0]
  bb_004728EC[BB_004728EC]
  bb_004728F1[BB_004728F1]
  bb_004728FB[BB_004728FB]
  bb_004728FC[BB_004728FC]
  bb_004728C0 -->|branch| bb_004728FC
  bb_004728C0 -->|fallthrough| bb_004728EC
  bb_004728EC -->|flow| bb_004728F1
  bb_004728FB -->|flow| bb_004728FC
  bb_004728FC -->|branch| bb_004728F1
```
