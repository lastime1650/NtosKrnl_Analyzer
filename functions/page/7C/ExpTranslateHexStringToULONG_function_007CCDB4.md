# ExpTranslateHexStringToULONG

- RVA: `0x007CCDB4`–`0x007CCE4A` (길이 `150` bytes)
- VA: `0x00000001407CCDB4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F3F8`
- 디코드: `49`개 명령, `150/150` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007CCDF4` → [towlower](../../text/50/towlower_function_005018E0.md) (function, `0x005018E0`)

### Direct callers
- [ExpParseSignatureName](ExpParseSignatureName_function_007CBA30.md) at `0x007CBB39`
- [ExpParseSignatureName](ExpParseSignatureName_function_007CBA30.md) at `0x007CBBE8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007CCDF4` → [towlower](../../text/50/towlower_function_005018E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007CCDB4  48 8B C4                        mov rax, rsp
007CCDB7  48 89 58 08                     mov qword ptr [rax + 8], rbx
007CCDBB  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
007CCDBF  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
007CCDC3  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
007CCDC7  41 57                           push r15
007CCDC9  48 83 EC 20                     sub rsp, 0x20
007CCDCD  48 83 CF FF                     or rdi, 0xffffffffffffffff
007CCDD1  4C 8B FA                        mov r15, rdx
007CCDD4  33 DB                           xor ebx, ebx
007CCDD6  4C 8B F1                        mov r14, rcx
007CCDD9  48 FF C7                        inc rdi
007CCDDC  66 39 1C 79                     cmp word ptr [rcx + rdi*2], bx
007CCDE0  75 F7                           jne 0x1407ccdd9
007CCDE2  83 FF 08                        cmp edi, 8
007CCDE5  77 42                           ja 0x1407cce29
007CCDE7  8B F3                           mov esi, ebx
007CCDE9  3B F7                           cmp esi, edi
007CCDEB  73 35                           jae 0x1407cce22
007CCDED  8B CE                           mov ecx, esi
007CCDEF  41 0F B7 0C 4E                  movzx ecx, word ptr [r14 + rcx*2]
007CCDF4  E8 E7 4A D3 FF                  call 0x1405018e0
007CCDF9  0F B7 D0                        movzx edx, ax
007CCDFC  8D 4A D0                        lea ecx, [rdx - 0x30]
007CCDFF  66 83 F9 09                     cmp cx, 9
007CCE03  77 08                           ja 0x1407cce0d
007CCE05  C1 E3 04                        shl ebx, 4
007CCE08  83 C3 D0                        add ebx, -0x30
007CCE0B  EB 0F                           jmp 0x1407cce1c
007CCE0D  8D 42 9F                        lea eax, [rdx - 0x61]
007CCE10  66 83 F8 05                     cmp ax, 5
007CCE14  77 13                           ja 0x1407cce29
007CCE16  C1 E3 04                        shl ebx, 4
007CCE19  83 C3 A9                        add ebx, -0x57
007CCE1C  03 DA                           add ebx, edx
007CCE1E  FF C6                           inc esi
007CCE20  EB C7                           jmp 0x1407ccde9
007CCE22  41 89 1F                        mov dword ptr [r15], ebx
007CCE25  33 C0                           xor eax, eax
007CCE27  EB 05                           jmp 0x1407cce2e
007CCE29  B8 0D 00 00 C0                  mov eax, 0xc000000d
007CCE2E  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
007CCE33  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
007CCE38  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
007CCE3D  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
007CCE42  48 83 C4 20                     add rsp, 0x20
007CCE46  41 5F                           pop r15
007CCE48  C3                              ret
007CCE49  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpTranslateHexStringToULONG(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = v_r14;
    v_rsp = (v_rsp) - (32);
    v_rdi = (v_rdi) | (-1);
    v_rbx = 0;
loc_007CCDD9:
    v_rdi = (v_rdi) + 1;
    if ((*(unsigned __int16 *)(a1 + v_rdi * 2)) != 0) goto loc_007CCDD9;
    if (((unsigned int)(v_rdi)) > 8) goto loc_007CCE29;
loc_007CCDE9:
    if (0 >= ((unsigned int)(v_rdi))) goto loc_007CCE22;
    result = towlower(*(unsigned __int16 *)(a1 + 0 * 2), a2, a3, a4);
    if (((unsigned __int16)((unsigned __int16)(result) - 48)) > 9) goto loc_007CCE0D;
    v_rbx = (unsigned int)((v_rbx) << (4));
    v_rbx = (unsigned int)((v_rbx) + (-48));
    goto loc_007CCE1C;
loc_007CCE0D:
    if (((unsigned __int16)((unsigned __int16)(result) - 97)) > 5) goto loc_007CCE29;
    v_rbx = (unsigned int)((v_rbx) << (4));
    v_rbx = (unsigned int)((v_rbx) + (-87));
loc_007CCE1C:
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)((unsigned __int16)(result))));
    v_rsi = (unsigned int)((0) + 1);
    goto loc_007CCDE9;
loc_007CCE22:
    *(unsigned int *)(a2) = (unsigned int)(v_rbx);
    result = 0;
    goto loc_007CCE2E;
loc_007CCE29:
loc_007CCE2E:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(0xC000000DULL);
}
```

## 5. (Beta) C Style

```c
int64_t ExpTranslateHexStringToULONG(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = local_r14;
    local_rsp = (local_rsp) - (32);
    local_rdi = (local_rdi) | (-1);
    local_rbx = 0;
loc_007CCDD9:
    local_rdi = (local_rdi) + 1;
    if ((*(uint16_t *)(arg1 + local_rdi * 2)) != 0) goto loc_007CCDD9;
    if (((uint32_t)(local_rdi)) > 8) goto loc_007CCE29;
loc_007CCDE9:
    if (0 >= ((uint32_t)(local_rdi))) goto loc_007CCE22;
    result = towlower(*(uint16_t *)(arg1 + 0x0 * 2), Arg2, a3, a4);
    if (((uint16_t)((uint16_t)(result) - 48)) > 9) goto loc_007CCE0D;
    local_rbx = (uint32_t)((local_rbx) << (4));
    local_rbx = (uint32_t)((local_rbx) + (-48));
    goto loc_007CCE1C;
loc_007CCE0D:
    if (((uint16_t)((uint16_t)(result) - 97)) > 5) goto loc_007CCE29;
    local_rbx = (uint32_t)((local_rbx) << (4));
    local_rbx = (uint32_t)((local_rbx) + (-87));
loc_007CCE1C:
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)((uint16_t)(result))));
    local_rsi = (uint32_t)((0) + 1);
    goto loc_007CCDE9;
loc_007CCE22:
    *(uint32_t *)(arg2) = (uint32_t)(local_rbx);
    result = 0;
    goto loc_007CCE2E;
loc_007CCE29:
loc_007CCE2E:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(0xC000000DULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rcx*2` | `16` | `R` |
| `Arg1` | `+ 0x0 + rdi*2` | `16` | `R` |
| `Arg2` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007CCDB4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007CCDB4[BB_007CCDB4]
  bb_007CCDD9[BB_007CCDD9]
  bb_007CCDE2[BB_007CCDE2]
  bb_007CCDE7[BB_007CCDE7]
  bb_007CCDE9[BB_007CCDE9]
  bb_007CCDED[BB_007CCDED]
  bb_007CCE05[BB_007CCE05]
  bb_007CCE0D[BB_007CCE0D]
  bb_007CCE16[BB_007CCE16]
  bb_007CCE1C[BB_007CCE1C]
  bb_007CCE22[BB_007CCE22]
  bb_007CCE29[BB_007CCE29]
  bb_007CCE2E[BB_007CCE2E]
  bb_007CCE49[BB_007CCE49]
  bb_007CCDB4 -->|flow| bb_007CCDD9
  bb_007CCDD9 -->|branch| bb_007CCDD9
  bb_007CCDD9 -->|fallthrough| bb_007CCDE2
  bb_007CCDE2 -->|branch| bb_007CCE29
  bb_007CCDE2 -->|fallthrough| bb_007CCDE7
  bb_007CCDE7 -->|flow| bb_007CCDE9
  bb_007CCDE9 -->|branch| bb_007CCE22
  bb_007CCDE9 -->|fallthrough| bb_007CCDED
  bb_007CCDED -->|branch| bb_007CCE0D
  bb_007CCDED -->|fallthrough| bb_007CCE05
  bb_007CCE05 -->|branch| bb_007CCE1C
  bb_007CCE0D -->|branch| bb_007CCE29
  bb_007CCE0D -->|fallthrough| bb_007CCE16
  bb_007CCE16 -->|flow| bb_007CCE1C
  bb_007CCE1C -->|branch| bb_007CCDE9
  bb_007CCE22 -->|branch| bb_007CCE2E
  bb_007CCE29 -->|flow| bb_007CCE2E
```
