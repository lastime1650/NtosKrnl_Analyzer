# MiStrongCodeImage

- RVA: `0x004BE728`–`0x004BE786` (길이 `94` bytes)
- VA: `0x00000001404BE728`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009A3D0`
- 디코드: `29`개 명령, `94/94` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BE740` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x004BE75E` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)

### Direct callers
- [MiValidateSectionCreate](../../page/94/MiValidateSectionCreate_function_00940190.md) at `0x0094082A`
- [MiValidateSectionCreate](../../page/94/MiValidateSectionCreate_function_00940190.md) at `0x00940D07`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BE728  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004BE72D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
004BE732  57                              push rdi
004BE733  48 83 EC 20                     sub rsp, 0x20
004BE737  48 8B F9                        mov rdi, rcx
004BE73A  8B DA                           mov ebx, edx
004BE73C  48 83 C1 48                     add rcx, 0x48
004BE740  E8 4B 9F D8 FF                  call 0x140248690
004BE745  8B 57 5C                        mov edx, dword ptr [rdi + 0x5c]
004BE748  44 8B C2                        mov r8d, edx
004BE74B  41 C1 E8 12                     shr r8d, 0x12
004BE74F  41 83 E0 03                     and r8d, 3
004BE753  44 3B C3                        cmp r8d, ebx
004BE756  72 1C                           jb 0x1404be774
004BE758  8A D0                           mov dl, al
004BE75A  48 8D 4F 48                     lea rcx, [rdi + 0x48]
004BE75E  E8 5D 9B D8 FF                  call 0x1402482c0
004BE763  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004BE768  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
004BE76D  48 83 C4 20                     add rsp, 0x20
004BE771  5F                              pop rdi
004BE772  C3                              ret
004BE773  CC                              int3
004BE774  C1 E3 12                        shl ebx, 0x12
004BE777  33 DA                           xor ebx, edx
004BE779  81 E3 00 00 0C 00               and ebx, 0xc0000
004BE77F  33 DA                           xor ebx, edx
004BE781  89 5F 5C                        mov dword ptr [rdi + 0x5c], ebx
004BE784  EB D2                           jmp 0x1404be758
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiStrongCodeImage(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (72);
    result = ExAcquireSpinLockExclusive(a1, a2, a3, a4);
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 92))))) >> (18));
    a3 = (unsigned int)((a3) & (3));
    if (((unsigned int)(a3)) < ((unsigned int)((unsigned int)(a2)))) goto loc_004BE774;
loc_004BE758:
    result = MiReleaseSpinLockExclusive(a1 + 72, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_004BE774:
    v_rbx = (unsigned int)((v_stack_p8) << (18));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)((unsigned __int8)(result))));
    v_rbx = (unsigned int)((v_rbx) & (0xC0000ULL));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)((unsigned __int8)(result))));
    *(unsigned int *)(a1 + 92) = (unsigned int)(v_rbx);
    goto loc_004BE758;
}
```

## 5. (Beta) C Style

```c
int64_t MiStrongCodeImage(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (72);
    result = ExAcquireSpinLockExclusive(Arg1, Arg2, a3, a4);
    a3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5C))))) >> (18));
    a3 = (uint32_t)((a3) & (3));
    if (((uint32_t)(a3)) < ((uint32_t)((uint32_t)(Arg2)))) goto loc_004BE774;
loc_004BE758:
    result = MiReleaseSpinLockExclusive(Arg1 + 72, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_004BE774:
    local_rbx = (uint32_t)((v_stack_p8) << (18));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)((uint8_t)(result))));
    local_rbx = (uint32_t)((local_rbx) & (0xC0000ULL));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)((uint8_t)(result))));
    *(uint32_t *)(arg1 + 0x5C) = (uint32_t)(local_rbx);
    goto loc_004BE758;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x5C` | `32` | `R` |
| `Arg1` | `+ 0x5C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BE728&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BE728[BB_004BE728]
  bb_004BE758[BB_004BE758]
  bb_004BE773[BB_004BE773]
  bb_004BE774[BB_004BE774]
  bb_004BE728 -->|branch| bb_004BE774
  bb_004BE728 -->|fallthrough| bb_004BE758
  bb_004BE773 -->|flow| bb_004BE774
  bb_004BE774 -->|branch| bb_004BE758
```
