# KiHandleBound

- RVA: `0x005B1FB0`–`0x005B200E` (길이 `94` bytes)
- VA: `0x00000001405B1FB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `25`개 명령, `94/94` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005B1FD4` → [ExReferenceCallBackBlock](../2F/ExReferenceCallBackBlock_function_002F0040.md) (function, `0x002F0040`)
- `0x005B1FE5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005B1FF6` → [ExDereferenceCallBackBlock](../44/ExDereferenceCallBackBlock_function_0044D730.md) (function, `0x0044D730`)
- `0x005B1FFB` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [KiBoundFault](../6B/KiBoundFault_function_006BE040.md) at `0x006BE385`

### Static image references
- `0x005B1FC3` → RVA `0x00F475B8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B1FB0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005B1FB5  57                              push rdi
005B1FB6  48 83 EC 20                     sub rsp, 0x20
005B1FBA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
005B1FC3  48 8D 0D EE 55 99 00            lea rcx, [rip + 0x9955ee]
005B1FCA  33 DB                           xor ebx, ebx
005B1FCC  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
005B1FD3  90                              nop
005B1FD4  E8 67 E0 D3 FF                  call 0x1402f0040
005B1FD9  48 8B F8                        mov rdi, rax
005B1FDC  48 85 C0                        test rax, rax
005B1FDF  74 1A                           je 0x1405b1ffb
005B1FE1  48 8B 40 08                     mov rax, qword ptr [rax + 8]
005B1FE5  E8 E6 8A 10 00                  call 0x1406baad0
005B1FEA  48 8B D7                        mov rdx, rdi
005B1FED  48 8D 0D C4 55 99 00            lea rcx, [rip + 0x9955c4]
005B1FF4  8B D8                           mov ebx, eax
005B1FF6  E8 35 B7 E9 FF                  call 0x14044d730
005B1FFB  E8 B0 B8 CA FF                  call 0x14025d8b0
005B2000  8B C3                           mov eax, ebx
005B2002  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005B2007  48 83 C4 20                     add rsp, 0x20
005B200B  5F                              pop rdi
005B200C  C3                              ret
005B200D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiHandleBound(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    result = ExReferenceCallBackBlock(v_rip + 10049006, a2, a3, a4);
    if (result != 0) {
        result = *(unsigned __int64 *)(result + 8);
        result = guard_dispatch_icall(v_rip + 10049006, a2, a3, a4);
        a2 = result;
        a1 = v_rip + 10048964;
        v_rbx = (unsigned int)(result);
        result = ExDereferenceCallBackBlock(a1, a2, a3, a4);
    }
    result = KeLeaveCriticalRegion(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
void KiHandleBound(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    result = ExReferenceCallBackBlock(v_rip + 10049006, a2, a3, a4);
    if (result != 0) {
        result = *(uint64_t *)(result + 0x8);
        result = guard_dispatch_icall(v_rip + 10049006, a2, a3, a4);
        a2 = result;
        a1 = v_rip + 10048964;
        local_rbx = (uint32_t)(result);
        result = ExDereferenceCallBackBlock(a1, a2, a3, a4);
    }
    result = KeLeaveCriticalRegion(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B1FB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B1FB0[BB_005B1FB0]
  bb_005B1FE1[BB_005B1FE1]
  bb_005B1FFB[BB_005B1FFB]
  bb_005B200D[BB_005B200D]
  bb_005B1FB0 -->|branch| bb_005B1FFB
  bb_005B1FB0 -->|fallthrough| bb_005B1FE1
  bb_005B1FE1 -->|flow| bb_005B1FFB
```
