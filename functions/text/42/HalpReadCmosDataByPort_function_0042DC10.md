# HalpReadCmosDataByPort

- RVA: `0x0042DC10`–`0x0042DC6E` (길이 `94` bytes)
- VA: `0x000000014042DC10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B600`
- 디코드: `33`개 명령, `94/94` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0042DC2C` → [HalpAcquireCmosSpinLock](HalpAcquireCmosSpinLock_function_0042DEE8.md) (function, `0x0042DEE8`)
- `0x0042DC38` → [HalpReleaseCmosSpinLock](HalpReleaseCmosSpinLock_function_0042DE04.md) (function, `0x0042DE04`)

### Direct callers
- [HalpReadStdCmosData](HalpReadStdCmosData_function_0042DBF0.md) at `0x0042DBFF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0042DC10  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0042DC15  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0042DC1A  57                              push rdi
0042DC1B  48 83 EC 20                     sub rsp, 0x20
0042DC1F  8B 7C 24 50                     mov edi, dword ptr [rsp + 0x50]
0042DC23  49 8B F1                        mov rsi, r9
0042DC26  41 03 F8                        add edi, r8d
0042DC29  41 8B D8                        mov ebx, r8d
0042DC2C  E8 B7 02 00 00                  call 0x14042dee8
0042DC31  45 33 C0                        xor r8d, r8d
0042DC34  3B DF                           cmp ebx, edi
0042DC36  72 19                           jb 0x14042dc51
0042DC38  E8 C7 01 00 00                  call 0x14042de04
0042DC3D  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0042DC42  41 8B C0                        mov eax, r8d
0042DC45  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
0042DC4A  48 83 C4 20                     add rsp, 0x20
0042DC4E  5F                              pop rdi
0042DC4F  C3                              ret
0042DC50  CC                              int3
0042DC51  90                              nop
0042DC52  8A C3                           mov al, bl
0042DC54  BA 70 00 00 00                  mov edx, 0x70
0042DC59  FF C3                           inc ebx
0042DC5B  EE                              out dx, al
0042DC5C  90                              nop
0042DC5D  BA 71 00 00 00                  mov edx, 0x71
0042DC62  90                              nop
0042DC63  EC                              in al, dx
0042DC64  90                              nop
0042DC65  41 88 04 30                     mov byte ptr [r8 + rsi], al
0042DC69  41 FF C0                        inc r8d
0042DC6C  EB C6                           jmp 0x14042dc34
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpReadCmosDataByPort(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rdi = (unsigned int)(((unsigned int)(a5)) + (a3));
    result = HalpAcquireCmosSpinLock(a1, a2, a3, a4);
    a3 = 0;
loc_0042DC34:
    if (((unsigned int)((unsigned int)(a3))) < ((unsigned int)(v_rdi))) goto loc_0042DC51;
    result = HalpReleaseCmosSpinLock(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return 0;
loc_0042DC51:
    v_rbx = (unsigned int)((v_stack_p8) + 1);
    *(unsigned __int8 *)(a3 + v_stack_p10 * 1) = (unsigned __int8)((unsigned __int8)(v_stack_p8));
    a3 = (unsigned int)((a3) + 1);
    goto loc_0042DC34;
}
```

## 5. (Beta) C Style

```c
int64_t HalpReadCmosDataByPort(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rdi = (uint32_t)(((uint32_t)(Arg5)) + (Arg3));
    result = HalpAcquireCmosSpinLock(Arg1, Arg2, Arg3, Arg4);
    Arg3 = 0;
loc_0042DC34:
    if (((uint32_t)((uint32_t)(Arg3))) < ((uint32_t)(local_rdi))) goto loc_0042DC51;
    result = HalpReleaseCmosSpinLock(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (32);
    return 0;
loc_0042DC51:
    local_rbx = (uint32_t)((v_stack_p8) + 1);
    *(uint8_t *)(Arg3 + v_stack_p10 * 1) = (uint8_t)((uint8_t)(v_stack_p8));
    Arg3 = (uint32_t)((Arg3) + 1);
    goto loc_0042DC34;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042DC10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0042DC10[BB_0042DC10]
  bb_0042DC34[BB_0042DC34]
  bb_0042DC38[BB_0042DC38]
  bb_0042DC50[BB_0042DC50]
  bb_0042DC51[BB_0042DC51]
  bb_0042DC10 -->|flow| bb_0042DC34
  bb_0042DC34 -->|branch| bb_0042DC51
  bb_0042DC34 -->|fallthrough| bb_0042DC38
  bb_0042DC50 -->|flow| bb_0042DC51
  bb_0042DC51 -->|branch| bb_0042DC34
```
