# KseSetCompletionHook

- RVA: `0x004A81C0`–`0x004A824E` (길이 `142` bytes)
- VA: `0x00000001404A81C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069AD0`
- 디코드: `38`개 명령, `142/142` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004A81E5` → [KsepPoolAllocateNonPaged](KsepPoolAllocateNonPaged_function_004A8254.md) (function, `0x004A8254`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004A821C` → RVA `0x004AA950` (`KsepCompletionSafeWrapper`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A81C0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004A81C5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
004A81CA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
004A81CF  57                              push rdi
004A81D0  48 83 EC 20                     sub rsp, 0x20
004A81D4  48 8B E9                        mov rbp, rcx
004A81D7  49 8B D9                        mov rbx, r9
004A81DA  B9 30 00 00 00                  mov ecx, 0x30
004A81DF  49 8B F8                        mov rdi, r8
004A81E2  48 8B F2                        mov rsi, rdx
004A81E5  E8 6A 00 00 00                  call 0x1404a8254
004A81EA  4C 8B D0                        mov r10, rax
004A81ED  48 85 C0                        test rax, rax
004A81F0  74 55                           je 0x1404a8247
004A81F2  48 8B 8E B8 00 00 00            mov rcx, qword ptr [rsi + 0xb8]
004A81F9  48 89 28                        mov qword ptr [rax], rbp
004A81FC  48 89 78 08                     mov qword ptr [rax + 8], rdi
004A8200  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
004A8204  48 8B 41 38                     mov rax, qword ptr [rcx + 0x38]
004A8208  49 89 42 18                     mov qword ptr [r10 + 0x18], rax
004A820C  48 8B 41 40                     mov rax, qword ptr [rcx + 0x40]
004A8210  49 89 42 20                     mov qword ptr [r10 + 0x20], rax
004A8214  0F B6 41 03                     movzx eax, byte ptr [rcx + 3]
004A8218  41 89 42 28                     mov dword ptr [r10 + 0x28], eax
004A821C  48 8D 05 2D 27 00 00            lea rax, [rip + 0x272d]
004A8223  48 89 41 38                     mov qword ptr [rcx + 0x38], rax
004A8227  33 C0                           xor eax, eax
004A8229  4C 89 51 40                     mov qword ptr [rcx + 0x40], r10
004A822D  C6 41 03 E0                     mov byte ptr [rcx + 3], 0xe0
004A8231  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004A8236  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
004A823B  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
004A8240  48 83 C4 20                     add rsp, 0x20
004A8244  5F                              pop rdi
004A8245  C3                              ret
004A8246  CC                              int3
004A8247  B8 9A 00 00 C0                  mov eax, 0xc000009a
004A824C  EB E3                           jmp 0x1404a8231
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KseSetCompletionHook(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = KsepPoolAllocateNonPaged(48, a2, a3, a4);
    if (result == 0) goto loc_004A8247;
    *(unsigned __int64 *)(result) = a1;
    *(unsigned __int64 *)(result + 8) = a3;
    *(unsigned __int64 *)(result + 16) = a4;
    *(unsigned __int64 *)(result + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 56);
    *(unsigned __int64 *)(result + 32) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 64);
    *(unsigned int *)(result + 40) = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 184) + 3));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 56) = v_rip + 10029;
    result = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 184) + 64) = 0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 184) + 3) = 224;
loc_004A8231:
    v_rsp = (v_rsp) + (32);
    return result;
loc_004A8247:
    goto loc_004A8231;
}
```

## 5. (Beta) C Style

```c
int64_t KseSetCompletionHook(int64_t Arg1, void *Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = KsepPoolAllocateNonPaged(48, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_004A8247;
    *(uint64_t *)(result) = Arg1;
    *(uint64_t *)(result + 0x8) = Arg3;
    *(uint64_t *)(result + 0x10) = Arg4;
    *(uint64_t *)(result + 0x18) = *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x38);
    *(uint64_t *)(result + 0x20) = *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x40);
    *(uint32_t *)(result + 0x28) = (uint32_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x3));
    *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x38) = v_rip + 10029;
    result = 0;
    *(uint64_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x40) = 0;
    *(uint8_t *)(*(uint64_t *)(arg2 + 0xB8) + 0x3) = 224;
loc_004A8231:
    local_rsp = (local_rsp) + (32);
    return result;
loc_004A8247:
    goto loc_004A8231;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A81C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A81C0[BB_004A81C0]
  bb_004A81F2[BB_004A81F2]
  bb_004A8231[BB_004A8231]
  bb_004A8246[BB_004A8246]
  bb_004A8247[BB_004A8247]
  bb_004A81C0 -->|branch| bb_004A8247
  bb_004A81C0 -->|fallthrough| bb_004A81F2
  bb_004A81F2 -->|flow| bb_004A8231
  bb_004A8246 -->|flow| bb_004A8247
  bb_004A8247 -->|branch| bb_004A8231
```
