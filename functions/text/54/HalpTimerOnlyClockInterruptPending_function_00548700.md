# HalpTimerOnlyClockInterruptPending

- RVA: `0x00548700`–`0x00548749` (길이 `73` bytes)
- VA: `0x0000000140548700`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BF520`
- 디코드: `24`개 명령, `73/73` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00548718` → [HalpInterruptGetHighestPriorityInterrupt](HalpInterruptGetHighestPriorityInterrupt_function_00543F90.md) (function, `0x00543F90`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00548700  48 8B C4                        mov rax, rsp
00548703  53                              push rbx
00548704  48 83 EC 20                     sub rsp, 0x20
00548708  33 DB                           xor ebx, ebx
0054870A  48 8D 50 08                     lea rdx, [rax + 8]
0054870E  48 8D 48 10                     lea rcx, [rax + 0x10]
00548712  89 58 10                        mov dword ptr [rax + 0x10], ebx
00548715  88 58 08                        mov byte ptr [rax + 8], bl
00548718  E8 73 B8 FF FF                  call 0x140543f90
0054871D  85 C0                           test eax, eax
0054871F  78 1F                           js 0x140548740
00548721  38 5C 24 30                     cmp byte ptr [rsp + 0x30], bl
00548725  74 19                           je 0x140548740
00548727  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
0054872B  B9 01 00 00 00                  mov ecx, 1
00548730  05 2F FF FF FF                  add eax, 0xffffff2f
00548735  0F B6 DB                        movzx ebx, bl
00548738  A9 FD FF FF FF                  test eax, 0xfffffffd
0054873D  0F 44 D9                        cmove ebx, ecx
00548740  8A C3                           mov al, bl
00548742  48 83 C4 20                     add rsp, 0x20
00548746  5B                              pop rbx
00548747  C3                              ret
00548748  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpTimerOnlyClockInterruptPending(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_p10;
    unsigned __int8 v_stack_p8;

    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    *(unsigned int *)(v_rsp + 16) = 0;
    *(unsigned __int8 *)(v_rsp + 8) = 0;
    result = HalpInterruptGetHighestPriorityInterrupt(v_rsp + 16, v_rsp + 8, a3, a4);
    if (sign_flag) goto loc_00548740;
    if (v_stack_p8 != 0) {
        result = v_stack_p10;
        a1 = 1;
        result = (unsigned int)((result) + (0xFFFFFF2FULL));
        v_rbx = 0;
        if ((((unsigned int)(result)) & (0xFFFFFFFDULL)) == 0) { v_rbx = (unsigned int)(a1); }
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_rbx);
}
```

## 5. (Beta) C Style

```c
void HalpTimerOnlyClockInterruptPending(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_p10;
    uint8_t v_stack_p8;

    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    *(uint32_t *)(local_rsp + 0x10) = 0;
    *(uint8_t *)(local_rsp + 0x8) = 0;
    result = HalpInterruptGetHighestPriorityInterrupt(local_rsp + 16, local_rsp + 8, a3, a4);
    if (sign_flag) goto loc_00548740;
    if (v_stack_p8 != 0) {
        result = v_stack_p10;
        a1 = 1;
        result = (uint32_t)((result) + (0xFFFFFF2FULL));
        local_rbx = 0;
        if ((((uint32_t)(result)) & (0xFFFFFFFDULL)) == 0) { local_rbx = (uint32_t)(a1); }
    }
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(local_rbx);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00548700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00548700[BB_00548700]
  bb_00548721[BB_00548721]
  bb_00548727[BB_00548727]
  bb_00548740[BB_00548740]
  bb_00548748[BB_00548748]
  bb_00548700 -->|branch| bb_00548740
  bb_00548700 -->|fallthrough| bb_00548721
  bb_00548721 -->|branch| bb_00548740
  bb_00548721 -->|fallthrough| bb_00548727
  bb_00548727 -->|flow| bb_00548740
```
