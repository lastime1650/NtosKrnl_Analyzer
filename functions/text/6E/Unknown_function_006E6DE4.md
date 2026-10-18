# sub_006E6DE4

- RVA: `0x006E6DE4`–`0x006E6E64` (길이 `128` bytes)
- VA: `0x00000001406E6DE4`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008BEA0`
- 디코드: `32`개 명령, `128/128` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E6DF5` → [NP_CONTEXT::NpLeafDerefInternal](../3A/NP_CONTEXT_NpLeafDerefInternal_function_003A9A70.md) (function, `0x003A9A70`)
- `0x006E6E38` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006E6E59` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x006E6E02` → [sub_003ADD08 + 0x35](../3A/Unknown_function_003ADD08.md) (`tail-transfer`)
  - `0x006E6E21` → [sub_003ADD08 + 0x35](../3A/Unknown_function_003ADD08.md) (`tail-transfer`)
  - `0x006E6E2A` → [sub_003ADD08 + 0x35](../3A/Unknown_function_003ADD08.md) (`tail-transfer`)
  - `0x006E6E45` → [sub_003ADD08 + 0x35](../3A/Unknown_function_003ADD08.md) (`tail-transfer`)
  - `0x006E6E5F` → [sub_003ADD08 + 0x35](../3A/Unknown_function_003ADD08.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E6DE4  48 8B 46 10                     mov rax, qword ptr [rsi + 0x10]
006E6DE8  83 38 FF                        cmp dword ptr [rax], -1
006E6DEB  74 0D                           je 0x1406e6dfa
006E6DED  48 8D 53 08                     lea rdx, [rbx + 8]
006E6DF1  48 8D 4E 10                     lea rcx, [rsi + 0x10]
006E6DF5  E8 76 2C CC FF                  call 0x1403a9a70
006E6DFA  48 8B 6E 10                     mov rbp, qword ptr [rsi + 0x10]
006E6DFE  83 7D 00 FF                     cmp dword ptr [rbp], -1
006E6E02  0F 84 35 6F CC FF               je 0x1403add3d
006E6E08  8B 43 08                        mov eax, dword ptr [rbx + 8]
006E6E0B  A8 01                           test al, 1
006E6E0D  74 3B                           je 0x1406e6e4a
006E6E0F  4C 8B 73 08                     mov r14, qword ptr [rbx + 8]
006E6E13  49 81 E6 00 F0 FF FF            and r14, 0xfffffffffffff000
006E6E1A  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
006E6E1E  48 85 D2                        test rdx, rdx
006E6E21  0F 84 16 6F CC FF               je 0x1403add3d
006E6E27  F6 C2 02                        test dl, 2
006E6E2A  0F 85 0D 6F CC FF               jne 0x1403add3d
006E6E30  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
006E6E34  48 8D 4E 10                     lea rcx, [rsi + 0x10]
006E6E38  E8 93 3C FD FF                  call 0x1406baad0
006E6E3D  41 83 4E 08 02                  or dword ptr [r14 + 8], 2
006E6E42  FF 4D 30                        dec dword ptr [rbp + 0x30]
006E6E45  E9 F3 6E CC FF                  jmp 0x1403add3d
006E6E4A  FF 4D 2C                        dec dword ptr [rbp + 0x2c]
006E6E4D  48 8D 4E 10                     lea rcx, [rsi + 0x10]
006E6E51  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
006E6E55  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
006E6E59  E8 72 3C FD FF                  call 0x1406baad0
006E6E5E  90                              nop
006E6E5F  E9 D9 6E CC FF                  jmp 0x1403add3d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E6DE4(void)
{
    __int64 result;
    __int64 v_r14;

    result = *(unsigned __int64 *)(v_rsi + 16);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rsi + 16))) != -1) {
        a2 = v_rbx + 8;
        a1 = v_rsi + 16;
        result = NP_CONTEXT__NpLeafDerefInternal(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 8)))) & (1)) == 0) goto loc_006E6E4A;
    v_r14 = (*(unsigned __int64 *)(v_rbx + 8)) & (0xFFFFFFFFFFFFF000ULL);
    result = guard_dispatch_icall(v_rsi + 16, *(unsigned __int64 *)(v_r14 + 8), a3, a4);
loc_006E6E4A:
    result = guard_dispatch_icall(v_rsi + 16, *(unsigned __int64 *)(v_rbx + 8), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006E6DE4(void)
{
    int64_t result;
    int64_t local_r14;

    result = *(uint64_t *)(local_rsi + 0x10);
    if ((*(uint32_t *)(*(uint64_t *)(local_rsi + 0x10))) != -1) {
        a2 = local_rbx + 8;
        a1 = local_rsi + 16;
        result = NP_CONTEXT__NpLeafDerefInternal(a1, a2, a3, a4);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x8)))) & (1)) == 0) goto loc_006E6E4A;
    local_r14 = (*(uint64_t *)(local_rbx + 0x8)) & (0xFFFFFFFFFFFFF000ULL);
    result = guard_dispatch_icall(local_rsi + 16, *(uint64_t *)(local_r14 + 0x8), a3, a4);
loc_006E6E4A:
    result = guard_dispatch_icall(local_rsi + 16, *(uint64_t *)(local_rbx + 0x8), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E6DE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E6DE4[BB_006E6DE4]
  bb_006E6DED[BB_006E6DED]
  bb_006E6DFA[BB_006E6DFA]
  bb_006E6E08[BB_006E6E08]
  bb_006E6E0F[BB_006E6E0F]
  bb_006E6E27[BB_006E6E27]
  bb_006E6E30[BB_006E6E30]
  bb_006E6E4A[BB_006E6E4A]
  bb_006E6DE4 -->|branch| bb_006E6DFA
  bb_006E6DE4 -->|fallthrough| bb_006E6DED
  bb_006E6DED -->|flow| bb_006E6DFA
  bb_006E6DFA -->|fallthrough| bb_006E6E08
  bb_006E6E08 -->|branch| bb_006E6E4A
  bb_006E6E08 -->|fallthrough| bb_006E6E0F
  bb_006E6E0F -->|fallthrough| bb_006E6E27
  bb_006E6E27 -->|fallthrough| bb_006E6E30
```
