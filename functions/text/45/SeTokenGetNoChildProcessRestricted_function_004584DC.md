# SeTokenGetNoChildProcessRestricted

- RVA: `0x004584DC`–`0x00458573` (길이 `151` bytes)
- VA: `0x00000001404584DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007F3F8`
- 디코드: `41`개 명령, `151/151` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00458518` → [ExAcquireResourceSharedLite](../21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00458527` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00458535` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)

### Direct callers
- [PspGetNoChildProcessRestrictedPolicy](../../page/A1/PspGetNoChildProcessRestrictedPolicy_function_00A172B8.md) at `0x00A172F2`
- [SeSubProcessToken](../../page/AA/SeSubProcessToken_function_00AAD570.md) at `0x00AAD687`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004584DC  48 8B C4                        mov rax, rsp
004584DF  48 89 58 08                     mov qword ptr [rax + 8], rbx
004584E3  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
004584E7  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
004584EB  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
004584EF  41 57                           push r15
004584F1  48 83 EC 20                     sub rsp, 0x20
004584F5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004584FE  48 8B F2                        mov rsi, rdx
00458501  48 8B D9                        mov rbx, rcx
00458504  B2 01                           mov dl, 1
00458506  4D 8B F9                        mov r15, r9
00458509  4D 8B F0                        mov r14, r8
0045850C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00458513  90                              nop
00458514  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00458518  E8 A3 96 DB FF                  call 0x140211bc0
0045851D  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00458521  8B BB C8 00 00 00               mov edi, dword ptr [rbx + 0xc8]
00458527  E8 E4 74 E0 FF                  call 0x14025fa10
0045852C  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00458535  E8 B6 6A E0 FF                  call 0x14025eff0
0045853A  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0045853F  8B C7                           mov eax, edi
00458541  C1 E8 13                        shr eax, 0x13
00458544  24 01                           and al, 1
00458546  88 06                           mov byte ptr [rsi], al
00458548  8B C7                           mov eax, edi
0045854A  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0045854F  C1 E8 14                        shr eax, 0x14
00458552  24 01                           and al, 1
00458554  C1 EF 15                        shr edi, 0x15
00458557  40 80 E7 01                     and dil, 1
0045855B  41 88 06                        mov byte ptr [r14], al
0045855E  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
00458563  41 88 3F                        mov byte ptr [r15], dil
00458566  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
0045856B  48 83 C4 20                     add rsp, 0x20
0045856F  41 5F                           pop r15
00458571  C3                              ret
00458572  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeTokenGetNoChildProcessRestricted(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rdi;
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
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(a1 + 48), 1, a3, a4);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), 1, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, a3, a4);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 200))))) >> (19));
    result = (unsigned __int8)((result) & (1));
    *(unsigned __int8 *)(a2) = (unsigned __int8)(result);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 200))))) >> (20));
    result = (unsigned __int8)((result) & (1));
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 200))) >> (21));
    v_rdi = (unsigned __int8)((v_rdi) & (1));
    *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
    *(unsigned __int8 *)(a4) = (unsigned __int8)(v_rdi);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SeTokenGetNoChildProcessRestricted(void *Arg1, void *Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rdi;
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
    result = ExAcquireResourceSharedLite(*(uint64_t *)(arg1 + 0x30), 1, Arg3, Arg4);
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), 1, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), 1, Arg3, Arg4);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC8))))) >> (19));
    result = (uint8_t)((result) & (1));
    *(uint8_t *)(arg2) = (uint8_t)(result);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC8))))) >> (20));
    result = (uint8_t)((result) & (1));
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC8))) >> (21));
    local_rdi = (uint8_t)((local_rdi) & (1));
    *(uint8_t *)(arg3) = (uint8_t)(result);
    *(uint8_t *)(arg4) = (uint8_t)(local_rdi);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0xC8` | `32` | `R` |
| `Arg2` | `+ 0x0` | `8` | `W` |
| `Arg3` | `+ 0x0` | `8` | `W` |
| `Arg4` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004584DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004584DC[BB_004584DC]
  bb_00458572[BB_00458572]
```
