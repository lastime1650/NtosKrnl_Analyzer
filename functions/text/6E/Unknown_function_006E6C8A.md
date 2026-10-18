# sub_006E6C8A

- RVA: `0x006E6C8A`–`0x006E6D09` (길이 `127` bytes)
- VA: `0x00000001406E6C8A`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008B954`
- 디코드: `32`개 명령, `127/127` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E6C9B` → [NP_CONTEXT::NpLeafDerefInternal](../3A/NP_CONTEXT_NpLeafDerefInternal_function_003A9A70.md) (function, `0x003A9A70`)
- `0x006E6CDD` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x006E6CFE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x006E6CA7` → [sub_003AB41E + 0x35](../3A/Unknown_function_003AB41E.md) (`tail-transfer`)
  - `0x006E6CC6` → [sub_003AB41E + 0x35](../3A/Unknown_function_003AB41E.md) (`tail-transfer`)
  - `0x006E6CCF` → [sub_003AB41E + 0x35](../3A/Unknown_function_003AB41E.md) (`tail-transfer`)
  - `0x006E6CEA` → [sub_003AB41E + 0x35](../3A/Unknown_function_003AB41E.md) (`tail-transfer`)
  - `0x006E6D04` → [sub_003AB41E + 0x35](../3A/Unknown_function_003AB41E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E6C8A  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
006E6C8E  83 38 FF                        cmp dword ptr [rax], -1
006E6C91  74 0D                           je 0x1406e6ca0
006E6C93  48 8D 53 08                     lea rdx, [rbx + 8]
006E6C97  49 8D 4E 10                     lea rcx, [r14 + 0x10]
006E6C9B  E8 D0 2D CC FF                  call 0x1403a9a70
006E6CA0  49 8B 76 10                     mov rsi, qword ptr [r14 + 0x10]
006E6CA4  83 3E FF                        cmp dword ptr [rsi], -1
006E6CA7  0F 84 A6 47 CC FF               je 0x1403ab453
006E6CAD  8B 43 08                        mov eax, dword ptr [rbx + 8]
006E6CB0  A8 01                           test al, 1
006E6CB2  74 3B                           je 0x1406e6cef
006E6CB4  4C 8B 7B 08                     mov r15, qword ptr [rbx + 8]
006E6CB8  49 81 E7 00 F0 FF FF            and r15, 0xfffffffffffff000
006E6CBF  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
006E6CC3  48 85 D2                        test rdx, rdx
006E6CC6  0F 84 87 47 CC FF               je 0x1403ab453
006E6CCC  F6 C2 02                        test dl, 2
006E6CCF  0F 85 7E 47 CC FF               jne 0x1403ab453
006E6CD5  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
006E6CD9  49 8D 4E 10                     lea rcx, [r14 + 0x10]
006E6CDD  E8 EE 3D FD FF                  call 0x1406baad0
006E6CE2  41 83 4F 08 02                  or dword ptr [r15 + 8], 2
006E6CE7  FF 4E 30                        dec dword ptr [rsi + 0x30]
006E6CEA  E9 64 47 CC FF                  jmp 0x1403ab453
006E6CEF  FF 4E 2C                        dec dword ptr [rsi + 0x2c]
006E6CF2  49 8D 4E 10                     lea rcx, [r14 + 0x10]
006E6CF6  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
006E6CFA  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
006E6CFE  E8 CD 3D FD FF                  call 0x1406baad0
006E6D03  90                              nop
006E6D04  E9 4A 47 CC FF                  jmp 0x1403ab453
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E6C8A(void)
{
    __int64 result;
    __int64 v_r15;

    result = *(unsigned __int64 *)(v_r14 + 16);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_r14 + 16))) != -1) {
        a2 = v_rbx + 8;
        a1 = v_r14 + 16;
        result = NP_CONTEXT__NpLeafDerefInternal(a1, a2, a3, a4);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rbx + 8)))) & (1)) == 0) goto loc_006E6CEF;
    v_r15 = (*(unsigned __int64 *)(v_rbx + 8)) & (0xFFFFFFFFFFFFF000ULL);
    result = guard_dispatch_icall(v_r14 + 16, *(unsigned __int64 *)(v_r15 + 8), a3, a4);
loc_006E6CEF:
    result = guard_dispatch_icall(v_r14 + 16, *(unsigned __int64 *)(v_rbx + 8), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006E6C8A(void)
{
    int64_t result;
    int64_t local_r15;

    result = *(uint64_t *)(local_r14 + 0x10);
    if ((*(uint32_t *)(*(uint64_t *)(local_r14 + 0x10))) != -1) {
        a2 = local_rbx + 8;
        a1 = local_r14 + 16;
        result = NP_CONTEXT__NpLeafDerefInternal(a1, a2, a3, a4);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x8)))) & (1)) == 0) goto loc_006E6CEF;
    local_r15 = (*(uint64_t *)(local_rbx + 0x8)) & (0xFFFFFFFFFFFFF000ULL);
    result = guard_dispatch_icall(local_r14 + 16, *(uint64_t *)(local_r15 + 0x8), a3, a4);
loc_006E6CEF:
    result = guard_dispatch_icall(local_r14 + 16, *(uint64_t *)(local_rbx + 0x8), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E6C8A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E6C8A[BB_006E6C8A]
  bb_006E6C93[BB_006E6C93]
  bb_006E6CA0[BB_006E6CA0]
  bb_006E6CAD[BB_006E6CAD]
  bb_006E6CB4[BB_006E6CB4]
  bb_006E6CCC[BB_006E6CCC]
  bb_006E6CD5[BB_006E6CD5]
  bb_006E6CEF[BB_006E6CEF]
  bb_006E6C8A -->|branch| bb_006E6CA0
  bb_006E6C8A -->|fallthrough| bb_006E6C93
  bb_006E6C93 -->|flow| bb_006E6CA0
  bb_006E6CA0 -->|fallthrough| bb_006E6CAD
  bb_006E6CAD -->|branch| bb_006E6CEF
  bb_006E6CAD -->|fallthrough| bb_006E6CB4
  bb_006E6CB4 -->|fallthrough| bb_006E6CCC
  bb_006E6CCC -->|fallthrough| bb_006E6CD5
```
