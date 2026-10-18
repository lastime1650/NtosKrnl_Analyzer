# MiCompleteSecureDriverLoad

- RVA: `0x00A4B920`–`0x00A4B99A` (길이 `122` bytes)
- VA: `0x0000000140A4B920`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B023C`
- 디코드: `31`개 명령, `122/122` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A4B93B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A4B972` → [VslCompleteSecureDriverLoad](VslCompleteSecureDriverLoad_function_00A4BB18.md) (function, `0x00A4BB18`)
- `0x00A4B981` → [MiUnlockDriverPages](MiUnlockDriverPages_function_00A4BA6C.md) (function, `0x00A4BA6C`)

### Direct callers
- [MiFinalizeDriverCfgState](MiFinalizeDriverCfgState_function_00A4AD54.md) at `0x00A4AD90`
- [MiMarkKernelImageCfgBits](MiMarkKernelImageCfgBits_function_00A4B1E0.md) at `0x00A4B22D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A4B93B` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A4B920  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A4B925  57                              push rdi
00A4B926  48 81 EC 90 00 00 00            sub rsp, 0x90
00A4B92D  33 D2                           xor edx, edx
00A4B92F  48 8B D9                        mov rbx, rcx
00A4B932  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A4B937  44 8D 42 68                     lea r8d, [rdx + 0x68]
00A4B93B  E8 00 B3 C7 FF                  call 0x1406c6c40
00A4B940  44 8B 43 40                     mov r8d, dword ptr [rbx + 0x40]
00A4B944  BF 00 00 00 00                  mov edi, 0
00A4B949  48 8B 4B 70                     mov rcx, qword ptr [rbx + 0x70]
00A4B94D  44 8B CF                        mov r9d, edi
00A4B950  41 8B D0                        mov edx, r8d
00A4B953  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A4B958  41 F7 C0 FF 0F 00 00            test r8d, 0xfff
00A4B95F  41 0F 95 C1                     setne r9b
00A4B963  C1 EA 0C                        shr edx, 0xc
00A4B966  44 03 CA                        add r9d, edx
00A4B969  48 8B 53 30                     mov rdx, qword ptr [rbx + 0x30]
00A4B96D  44 89 4C 24 38                  mov dword ptr [rsp + 0x38], r9d
00A4B972  E8 A1 01 00 00                  call 0x140a4bb18
00A4B977  85 C0                           test eax, eax
00A4B979  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00A4B97E  0F 48 F8                        cmovs edi, eax
00A4B981  E8 E6 00 00 00                  call 0x140a4ba6c
00A4B986  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
00A4B98E  8B C7                           mov eax, edi
00A4B990  48 81 C4 90 00 00 00            add rsp, 0x90
00A4B997  5F                              pop rdi
00A4B998  C3                              ret
00A4B999  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCompleteSecureDriverLoad(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (144);
    a2 = 0;
    result = memset(v_stack_m78, a2, a2 + 104, a4);
    v_stack_m78 = a1;
    a4 = ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64)))) & (0xFFFULL)) != 0) ? 1 : 0;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64))))) >> (12));
    a4 = (unsigned int)((a4) + (a2));
    v_stack_m60 = (unsigned int)(a4);
    result = VslCompleteSecureDriverLoad(*(unsigned __int64 *)(a1 + 112), *(unsigned __int64 *)(a1 + 48), (unsigned int)(*(unsigned int *)(a1 + 64)), a4);
    v_rdi = 0;
    if (sign_flag) { v_rdi = (unsigned int)(result); }
    result = MiUnlockDriverPages(v_stack_m78, *(unsigned __int64 *)(a1 + 48), (unsigned int)(*(unsigned int *)(a1 + 64)), a4);
    v_rsp = (v_rsp) + (144);
    return (unsigned int)((unsigned int)(v_rdi));
}
```

## 5. (Beta) C Style

```c
int64_t MiCompleteSecureDriverLoad(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint32_t v_stack_m60;
    uint64_t v_stack_m78;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (144);
    Arg2 = 0;
    result = memset(v_stack_m78, Arg2, Arg2 + 104, a4);
    v_stack_m78 = Arg1;
    a4 = ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)))) & (0xFFFULL)) != 0) ? 1 : 0;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40))))) >> (12));
    a4 = (uint32_t)((a4) + (Arg2));
    v_stack_m60 = (uint32_t)(a4);
    result = VslCompleteSecureDriverLoad(*(uint64_t *)(arg1 + 0x70), *(uint64_t *)(arg1 + 0x30), (uint32_t)(*(uint32_t *)(arg1 + 0x40)), a4);
    local_rdi = 0;
    if (sign_flag) { local_rdi = (uint32_t)(result); }
    result = MiUnlockDriverPages(v_stack_m78, *(uint64_t *)(arg1 + 0x30), (uint32_t)(*(uint32_t *)(arg1 + 0x40)), a4);
    local_rsp = (local_rsp) + (144);
    return (uint32_t)((uint32_t)(local_rdi));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4B920&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A4B920[BB_00A4B920]
  bb_00A4B999[BB_00A4B999]
```
