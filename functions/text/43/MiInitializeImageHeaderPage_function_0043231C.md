# MiInitializeImageHeaderPage

- RVA: `0x0043231C`–`0x004323AB` (길이 `143` bytes)
- VA: `0x000000014043231C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F908`
- 디코드: `39`개 명령, `143/143` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00432347` → [MiMapPageInHyperSpaceWorker](../33/MiMapPageInHyperSpaceWorker_function_00332B10.md) (function, `0x00332B10`)
- `0x0043235E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00432370` → [MiUnmapPageInHyperSpaceWorker](MiUnmapPageInHyperSpaceWorker_function_00432800.md) (function, `0x00432800`)

### Direct callers
- [MiCreateImageFileMap](../../page/98/MiCreateImageFileMap_function_00986830.md) at `0x00986C26`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0043231C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00432321  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
00432326  57                              push rdi
00432327  48 83 EC 20                     sub rsp, 0x20
0043232B  48 8B C2                        mov rax, rdx
0043232E  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
00432333  49 8B F8                        mov rdi, r8
00432336  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
0043233B  48 8B F1                        mov rsi, rcx
0043233E  41 B8 00 00 00 80               mov r8d, 0x80000000
00432344  48 8B C8                        mov rcx, rax
00432347  E8 C4 07 F0 FF                  call 0x140332b10
0043234C  41 B8 00 10 00 00               mov r8d, 0x1000
00432352  33 D2                           xor edx, edx
00432354  4C 2B C7                        sub r8, rdi
00432357  48 8B D8                        mov rbx, rax
0043235A  48 8D 0C 38                     lea rcx, [rax + rdi]
0043235E  E8 DD 48 29 00                  call 0x1406c6c40
00432363  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
00432367  41 B8 00 00 00 80               mov r8d, 0x80000000
0043236D  48 8B CB                        mov rcx, rbx
00432370  E8 8B 04 00 00                  call 0x140432800
00432375  48 F7 C7 FF 01 00 00            test rdi, 0x1ff
0043237C  75 11                           jne 0x14043238f
0043237E  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00432383  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
00432388  48 83 C4 20                     add rsp, 0x20
0043238C  5F                              pop rdi
0043238D  C3                              ret
0043238E  CC                              int3
0043238F  48 8B 56 60                     mov rdx, qword ptr [rsi + 0x60]
00432393  48 83 E2 F8                     and rdx, 0xfffffffffffffff8
00432397  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
0043239A  8B C8                           mov ecx, eax
0043239C  33 CF                           xor ecx, edi
0043239E  81 E1 FF 0F 00 00               and ecx, 0xfff
004323A4  33 C8                           xor ecx, eax
004323A6  89 4A 38                        mov dword ptr [rdx + 0x38], ecx
004323A9  EB D3                           jmp 0x14043237e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitializeImageHeaderPage(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int8 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_stack_p18 = 0;
    result = MiMapPageInHyperSpaceWorker(a2, v_stack_p18, (unsigned int)(0x80000000ULL), a4);
    a2 = 0;
    a3 = ((unsigned int)(0x1000ULL)) - (a3);
    result = memset(result + a3 * 1, a2, a3, a4);
    result = MiUnmapPageInHyperSpaceWorker(result, v_stack_p18, (unsigned int)(0x80000000ULL), a4);
    if (((a3) & (511)) != 0) goto loc_0043238F;
loc_0043237E:
    v_rsp = (v_rsp) + (32);
    return result;
loc_0043238F:
    a2 = (*(unsigned __int64 *)(v_stack_p10 + 96)) & (-8);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 56))))) ^ ((unsigned int)(a3)));
    a1 = (unsigned int)((a1) & (0xFFFULL));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 56)))));
    *(unsigned int *)(a2 + 56) = (unsigned int)(a1);
    goto loc_0043237E;
}
```

## 5. (Beta) C Style

```c
int64_t MiInitializeImageHeaderPage(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint8_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    v_stack_p18 = 0;
    result = MiMapPageInHyperSpaceWorker(Arg2, v_stack_p18, (uint32_t)(0x80000000ULL), a4);
    Arg2 = 0;
    Arg3 = ((uint32_t)(0x1000ULL)) - (Arg3);
    result = memset(result + Arg3 * 1, Arg2, Arg3, a4);
    result = MiUnmapPageInHyperSpaceWorker(result, v_stack_p18, (uint32_t)(0x80000000ULL), a4);
    if (((Arg3) & (511)) != 0) goto loc_0043238F;
loc_0043237E:
    local_rsp = (local_rsp) + (32);
    return result;
loc_0043238F:
    Arg2 = (*(uint64_t *)(v_stack_p10 + 0x60)) & (-8);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x38))))) ^ ((uint32_t)(Arg3)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFULL));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2 + 0x38)))));
    *(uint32_t *)(Arg2 + 0x38) = (uint32_t)(Arg1);
    goto loc_0043237E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x60` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043231C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043231C[BB_0043231C]
  bb_0043237E[BB_0043237E]
  bb_0043238E[BB_0043238E]
  bb_0043238F[BB_0043238F]
  bb_0043231C -->|branch| bb_0043238F
  bb_0043231C -->|fallthrough| bb_0043237E
  bb_0043238E -->|flow| bb_0043238F
  bb_0043238F -->|branch| bb_0043237E
```
