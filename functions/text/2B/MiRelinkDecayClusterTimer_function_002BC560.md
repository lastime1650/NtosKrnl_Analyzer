# MiRelinkDecayClusterTimer

- RVA: `0x002BC560`–`0x002BC693` (길이 `307` bytes)
- VA: `0x00000001402BC560`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E13C`
- 디코드: `72`개 명령, `307/307` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiInsertDecayClusterTimer](MiInsertDecayClusterTimer_function_002BADF4.md) at `0x002BAE2E`
- [MiEmptyDecayClusterTimers](../2D/MiEmptyDecayClusterTimers_function_002DAB50.md) at `0x002DAE2C`

### Static image references
- `0x002BC5A9` → RVA `0x00E30088` (`.data`; read)
- `0x002BC5EF` → RVA `0x00E35C00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002BC560  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002BC565  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
002BC56A  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
002BC56F  57                              push rdi
002BC570  44 8B 41 20                     mov r8d, dword ptr [rcx + 0x20]
002BC574  8A C2                           mov al, dl
002BC576  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
002BC57B  4C 8B C9                        mov r9, rcx
002BC57E  C0 E0 06                        shl al, 6
002BC581  41 C1 E8 10                     shr r8d, 0x10
002BC585  41 80 E0 3F                     and r8b, 0x3f
002BC589  44 8B DA                        mov r11d, edx
002BC58C  44 0A C0                        or r8b, al
002BC58F  48 BD 00 00 00 00 00 DE FF FF   movabs rbp, 0xffffde0000000000
002BC599  44 88 44 24 1A                  mov byte ptr [rsp + 0x1a], r8b
002BC59E  8B 44 24 18                     mov eax, dword ptr [rsp + 0x18]
002BC5A2  89 41 20                        mov dword ptr [rcx + 0x20], eax
002BC5A5  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
002BC5A9  48 8B 0D D8 3A B7 00            mov rcx, qword ptr [rip + 0xb73ad8]
002BC5B0  48 C1 E8 2B                     shr rax, 0x2b
002BC5B4  25 FF 03 00 00                  and eax, 0x3ff
002BC5B9  48 8B 1C C1                     mov rbx, qword ptr [rcx + rax*8]
002BC5BD  48 8B C5                        mov rax, rbp
002BC5C0  4D 8B D1                        mov r10, r9
002BC5C3  BE FE FF FF FF                  mov esi, 0xfffffffe
002BC5C8  4C 2B D0                        sub r10, rax
002BC5CB  48 BF 00 00 00 00 FE FF FF FF   movabs rdi, 0xfffffffe00000000
002BC5D5  49 C1 FA 04                     sar r10, 4
002BC5D9  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
002BC5E3  4C 0F AF D0                     imul r10, rax
002BC5E7  4A 8B 84 DB C0 3E 00 00         mov rax, qword ptr [rbx + r11*8 + 0x3ec0]
002BC5EF  4C 2B 15 0A 96 B7 00            sub r10, qword ptr [rip + 0xb7960a]
002BC5F6  48 8B D0                        mov rdx, rax
002BC5F9  48 23 D6                        and rdx, rsi
002BC5FC  4C 8B C0                        mov r8, rax
002BC5FF  49 D1 E8                        shr r8, 1
002BC602  48 8B CA                        mov rcx, rdx
002BC605  48 0B CF                        or rcx, rdi
002BC608  41 0F BA F0 1F                  btr r8d, 0x1f
002BC60D  49 89 49 08                     mov qword ptr [r9 + 8], rcx
002BC611  4D 8B CA                        mov r9, r10
002BC614  49 C1 E1 21                     shl r9, 0x21
002BC618  48 3B D6                        cmp rdx, rsi
002BC61B  74 64                           je 0x1402bc681
002BC61D  48 8B 15 DC 95 B7 00            mov rdx, qword ptr [rip + 0xb795dc]
002BC624  49 03 D0                        add rdx, r8
002BC627  4C 8D 04 52                     lea r8, [rdx + rdx*2]
002BC62B  49 C1 E0 04                     shl r8, 4
002BC62F  48 8B CD                        mov rcx, rbp
002BC632  4C 03 C1                        add r8, rcx
002BC635  48 BA FF FF FF FF 01 00 00 00   movabs rdx, 0x1ffffffff
002BC63F  49 8B 48 08                     mov rcx, qword ptr [r8 + 8]
002BC643  48 23 CA                        and rcx, rdx
002BC646  49 0B C9                        or rcx, r9
002BC649  49 89 48 08                     mov qword ptr [r8 + 8], rcx
002BC64D  48 8B 6C 24 20                  mov rbp, qword ptr [rsp + 0x20]
002BC652  4B 8D 0C 12                     lea rcx, [r10 + r10]
002BC656  48 8B 74 24 28                  mov rsi, qword ptr [rsp + 0x28]
002BC65B  48 8B D1                        mov rdx, rcx
002BC65E  48 33 D0                        xor rdx, rax
002BC661  48 B8 01 00 00 00 FF FF FF FF   movabs rax, 0xffffffff00000001
002BC66B  48 23 D0                        and rdx, rax
002BC66E  48 33 D1                        xor rdx, rcx
002BC671  4A 89 94 DB C0 3E 00 00         mov qword ptr [rbx + r11*8 + 0x3ec0], rdx
002BC679  48 8B 5C 24 10                  mov rbx, qword ptr [rsp + 0x10]
002BC67E  5F                              pop rdi
002BC67F  C3                              ret
002BC680  CC                              int3
002BC681  48 BA FF FF FF FF 01 00 00 00   movabs rdx, 0x1ffffffff
002BC68B  48 23 C2                        and rax, rdx
002BC68E  49 0B C1                        or rax, r9
002BC691  EB BA                           jmp 0x1402bc64d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiRelinkDecayClusterTimer(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r10;
    unsigned int v_stack_p10;
    unsigned __int8 v_stack_p12;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned __int8)(((unsigned __int8)(a2)) << (6));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    a3 = (unsigned __int8)((a3) & (63));
    a3 = (unsigned __int8)((a3) | ((unsigned __int8)(result)));
    v_stack_p12 = (unsigned __int8)(a3);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p10));
    result = (*(unsigned __int64 *)(a1 + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_r10 = (a1) - (v_rbp);
    v_r10 = (v_r10) >> (4);
    v_r10 = (v_r10) * (v_rbp);
    v_r10 = (v_r10) - (*(unsigned __int64 *)(v_rip + 12031498));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12008152) + result * 8) + (unsigned int)(a2) * 8 + 16064)) & ((unsigned int)(0xFFFFFFFEULL));
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12008152) + result * 8) + (unsigned int)(a2) * 8 + 16064)) >> (1);
    a1 = (a2) | (v_rdi);
    *(unsigned __int64 *)(a1 + 8) = a1;
    a4 = (v_r10) << (33);
    if (a2 == ((unsigned int)(0xFFFFFFFEULL))) goto loc_002BC681;
    a2 = (*(unsigned __int64 *)(v_rip + 12031452)) + (a3);
    a3 = (a2 + a2 * 2) << (4);
    a3 = (a3) + (v_rbp);
    a1 = (*(unsigned __int64 *)(a3 + 8)) & (a2);
    a1 = (a1) | (a4);
    *(unsigned __int64 *)(a3 + 8) = a1;
loc_002BC64D:
    a2 = (v_r10 + v_r10 * 1) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12008152) + result * 8) + (unsigned int)(a2) * 8 + 16064));
    a2 = (a2) & (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12008152) + result * 8) + (unsigned int)(a2) * 8 + 16064));
    a2 = (a2) ^ (v_r10 + v_r10 * 1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12008152) + result * 8) + (unsigned int)(a2) * 8 + 16064) = a2;
    return *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12008152) + result * 8) + (unsigned int)(a2) * 8 + 16064);
loc_002BC681:
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12008152) + result * 8) + (unsigned int)(a2) * 8 + 16064)) & (a2);
    result = (result) | (a4);
    goto loc_002BC64D;
}
```

## 5. (Beta) C Style

```c
int64_t MiRelinkDecayClusterTimer(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    uint32_t v_stack_p10;
    uint8_t v_stack_p12;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint8_t)(((uint8_t)(Arg2)) << (6));
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    a3 = (uint8_t)((a3) & (63));
    a3 = (uint8_t)((a3) | ((uint8_t)(result)));
    v_stack_p12 = (uint8_t)(a3);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p10));
    result = (*(uint64_t *)(arg1 + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    local_r10 = (Arg1) - (local_rbp);
    local_r10 = (local_r10) >> (4);
    local_r10 = (local_r10) * (local_rbp);
    local_r10 = (local_r10) - (*(uint64_t *)(v_rip + 0xB7960A));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB73AD8) + result * 8) + (uint32_t)(Arg2) * 8 + 0x3EC0)) & ((uint32_t)(0xFFFFFFFEULL));
    a3 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB73AD8) + result * 8) + (uint32_t)(Arg2) * 8 + 0x3EC0)) >> (1);
    Arg1 = (Arg2) | (local_rdi);
    *(void **)(arg1 + 0x8) = Arg1;
    a4 = (local_r10) << (33);
    if (Arg2 == ((uint32_t)(0xFFFFFFFEULL))) goto loc_002BC681;
    Arg2 = (*(uint64_t *)(v_rip + 0xB795DC)) + (a3);
    a3 = (Arg2 + Arg2 * 2) << (4);
    a3 = (a3) + (local_rbp);
    Arg1 = (*(uint64_t *)(a3 + 0x8)) & (Arg2);
    Arg1 = (Arg1) | (a4);
    *(void **)(a3 + 0x8) = Arg1;
loc_002BC64D:
    Arg2 = (local_r10 + local_r10 * 1) ^ (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB73AD8) + result * 8) + (uint32_t)(Arg2) * 8 + 0x3EC0));
    Arg2 = (Arg2) & (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB73AD8) + result * 8) + (uint32_t)(Arg2) * 8 + 0x3EC0));
    Arg2 = (Arg2) ^ (local_r10 + local_r10 * 1);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB73AD8) + result * 8) + (uint32_t)(Arg2) * 8 + 0x3EC0) = Arg2;
    return *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB73AD8) + result * 8) + (uint32_t)(Arg2) * 8 + 0x3EC0);
loc_002BC681:
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0xB73AD8) + result * 8) + (uint32_t)(Arg2) * 8 + 0x3EC0)) & (Arg2);
    result = (result) | (a4);
    goto loc_002BC64D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002BC560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002BC560[BB_002BC560]
  bb_002BC61D[BB_002BC61D]
  bb_002BC64D[BB_002BC64D]
  bb_002BC680[BB_002BC680]
  bb_002BC681[BB_002BC681]
  bb_002BC560 -->|branch| bb_002BC681
  bb_002BC560 -->|fallthrough| bb_002BC61D
  bb_002BC61D -->|flow| bb_002BC64D
  bb_002BC680 -->|flow| bb_002BC681
  bb_002BC681 -->|branch| bb_002BC64D
```
