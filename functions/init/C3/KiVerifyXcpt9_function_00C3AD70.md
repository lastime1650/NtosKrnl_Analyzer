# KiVerifyXcpt9

- RVA: `0x00C3AD70`–`0x00C3ADC7` (길이 `87` bytes)
- VA: `0x0000000140C3AD70`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CAF20`
- 디코드: `28`개 명령, `87/87` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C3AD70  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00C3AD75  48 83 EC 38                     sub rsp, 0x38
00C3AD79  48 89 64 24 20                  mov qword ptr [rsp + 0x20], rsp
00C3AD7E  48 8B D1                        mov rdx, rcx
00C3AD81  83 79 08 01                     cmp dword ptr [rcx + 8], 1
00C3AD85  74 0D                           je 0x140c3ad94
00C3AD87  83 49 0C FF                     or dword ptr [rcx + 0xc], 0xffffffff
00C3AD8B  C7 41 10 01 00 00 00            mov dword ptr [rcx + 0x10], 1
00C3AD92  EB 25                           jmp 0x140c3adb9
00C3AD94  48 8B 01                        mov rax, qword ptr [rcx]
00C3AD97  FF 00                           inc dword ptr [rax]
00C3AD99  EB 0E                           jmp 0x140c3ada9
00C3AD9B  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00C3ADA0  48 8B 02                        mov rax, qword ptr [rdx]
00C3ADA3  8B 08                           mov ecx, dword ptr [rax]
00C3ADA5  FF C1                           inc ecx
00C3ADA7  89 08                           mov dword ptr [rax], ecx
00C3ADA9  EB 0E                           jmp 0x140c3adb9
00C3ADAB  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00C3ADB0  48 8B 02                        mov rax, qword ptr [rdx]
00C3ADB3  8B 08                           mov ecx, dword ptr [rax]
00C3ADB5  FF C1                           inc ecx
00C3ADB7  89 08                           mov dword ptr [rax], ecx
00C3ADB9  48 63 42 0C                     movsxd rax, dword ptr [rdx + 0xc]
00C3ADBD  48 01 42 18                     add qword ptr [rdx + 0x18], rax
00C3ADC1  48 83 C4 38                     add rsp, 0x38
00C3ADC5  C3                              ret
00C3ADC6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiVerifyXcpt9(__int64 a1)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (56);
    v_stack_m18 = v_rsp;
    if ((*(unsigned int *)(a1 + 8)) == 1) goto loc_00C3AD94;
    *(unsigned int *)(a1 + 16) = 1;
    goto loc_00C3ADB9;
loc_00C3AD94:
    goto loc_00C3ADA9;
loc_00C3ADA9:
    goto loc_00C3ADB9;
loc_00C3ADB9:
    v_rsp = (v_rsp) + (56);
    return (int)(*(unsigned int *)(a1 + 12));
}
```

## 5. (Beta) C Style

```c
int64_t KiVerifyXcpt9(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (56);
    v_stack_m18 = local_rsp;
    if ((*(uint32_t *)(arg1 + 0x8)) == 1) goto loc_00C3AD94;
    *(uint32_t *)(arg1 + 0x10) = 1;
    goto loc_00C3ADB9;
loc_00C3AD94:
    goto loc_00C3ADA9;
loc_00C3ADA9:
    goto loc_00C3ADB9;
loc_00C3ADB9:
    local_rsp = (local_rsp) + (56);
    return (int32_t)(*(uint32_t *)(arg1 + 0xC));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R/W` |
| `Arg1` | `+ 0x10` | `32` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C3AD70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C3AD70[BB_00C3AD70]
  bb_00C3AD87[BB_00C3AD87]
  bb_00C3AD94[BB_00C3AD94]
  bb_00C3AD9B[BB_00C3AD9B]
  bb_00C3ADA9[BB_00C3ADA9]
  bb_00C3ADAB[BB_00C3ADAB]
  bb_00C3ADB9[BB_00C3ADB9]
  bb_00C3ADC6[BB_00C3ADC6]
  bb_00C3AD70 -->|branch| bb_00C3AD94
  bb_00C3AD70 -->|fallthrough| bb_00C3AD87
  bb_00C3AD87 -->|branch| bb_00C3ADB9
  bb_00C3AD94 -->|branch| bb_00C3ADA9
  bb_00C3AD9B -->|flow| bb_00C3ADA9
  bb_00C3ADA9 -->|branch| bb_00C3ADB9
  bb_00C3ADAB -->|flow| bb_00C3ADB9
```
