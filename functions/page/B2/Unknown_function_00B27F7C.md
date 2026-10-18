# sub_00B27F7C

- RVA: `0x00B27F7C`–`0x00B28052` (길이 `214` bytes)
- VA: `0x0000000140B27F7C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000933F4`
- 디코드: `55`개 명령, `214/214` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B27F81` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x00B27FFC` → [PiCMCaptureRegistryInputData + 0xED](../96/PiCMCaptureRegistryInputData_function_00962108.md) (`tail-transfer`)
  - `0x00B28027` → [PiCMCaptureRegistryInputData + 0xED](../96/PiCMCaptureRegistryInputData_function_00962108.md) (`tail-transfer`)
  - `0x00B28031` → [PiCMCaptureRegistryInputData + 0x161](../96/PiCMCaptureRegistryInputData_function_00962108.md) (`tail-transfer`)
  - `0x00B28037` → [PiCMCaptureRegistryInputData + 0x1E9](../96/PiCMCaptureRegistryInputData_function_00962108.md) (`tail-transfer`)
  - `0x00B2804D` → [PiCMCaptureRegistryInputData + 0x169](../96/PiCMCaptureRegistryInputData_function_00962108.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B27F7C  F6 C1 03                        test cl, 3
00B27F7F  74 05                           je 0x140b27f86
00B27F81  E8 4A 20 D7 FF                  call 0x140899fd0
00B27F86  44 8B C2                        mov r8d, edx
00B27F89  4C 03 C1                        add r8, rcx
00B27F8C  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
00B27F96  4C 3B C0                        cmp r8, rax
00B27F99  77 05                           ja 0x140b27fa0
00B27F9B  4C 3B C1                        cmp r8, rcx
00B27F9E  73 06                           jae 0x140b27fa6
00B27FA0  8A 00                           mov al, byte ptr [rax]
00B27FA2  8B 5C 24 34                     mov ebx, dword ptr [rsp + 0x34]
00B27FA6  BE 0D 00 00 C0                  mov esi, 0xc000000d
00B27FAB  83 FA 24                        cmp edx, 0x24
00B27FAE  72 46                           jb 0x140b27ff6
00B27FB0  83 39 24                        cmp dword ptr [rcx], 0x24
00B27FB3  75 41                           jne 0x140b27ff6
00B27FB5  41 C7 01 30 00 00 00            mov dword ptr [r9], 0x30
00B27FBC  8B 41 04                        mov eax, dword ptr [rcx + 4]
00B27FBF  41 89 41 04                     mov dword ptr [r9 + 4], eax
00B27FC3  8B 41 08                        mov eax, dword ptr [rcx + 8]
00B27FC6  41 89 41 08                     mov dword ptr [r9 + 8], eax
00B27FCA  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
00B27FCD  49 89 41 10                     mov qword ptr [r9 + 0x10], rax
00B27FD1  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
00B27FD4  41 89 41 18                     mov dword ptr [r9 + 0x18], eax
00B27FD8  8B 41 14                        mov eax, dword ptr [rcx + 0x14]
00B27FDB  41 89 41 1C                     mov dword ptr [r9 + 0x1c], eax
00B27FDF  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
00B27FE2  41 89 41 20                     mov dword ptr [r9 + 0x20], eax
00B27FE6  8B 41 1C                        mov eax, dword ptr [rcx + 0x1c]
00B27FE9  41 89 41 24                     mov dword ptr [r9 + 0x24], eax
00B27FED  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
00B27FF0  41 89 41 28                     mov dword ptr [r9 + 0x28], eax
00B27FF4  EB 06                           jmp 0x140b27ffc
00B27FF6  8B DE                           mov ebx, esi
00B27FF8  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
00B27FFC  E9 F4 A1 E3 FF                  jmp 0x1409621f5
00B28001  8B D8                           mov ebx, eax
00B28003  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00B28007  33 FF                           xor edi, edi
00B28009  BE 0D 00 00 C0                  mov esi, 0xc000000d
00B2800E  4C 8B B4 24 98 00 00 00         mov r14, qword ptr [rsp + 0x98]
00B28016  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
00B2801A  44 8A 64 24 30                  mov r12b, byte ptr [rsp + 0x30]
00B2801F  44 88 A4 24 80 00 00 00         mov byte ptr [rsp + 0x80], r12b
00B28027  E9 C9 A1 E3 FF                  jmp 0x1409621f5
00B2802C  41 83 3C 24 02                  cmp dword ptr [r12], 2
00B28031  0F 83 32 A2 E3 FF               jae 0x140962269
00B28037  E9 B5 A2 E3 FF                  jmp 0x1409622f1
00B2803C  0F 57 C0                        xorps xmm0, xmm0
00B2803F  41 0F 11 06                     movups xmmword ptr [r14], xmm0
00B28043  41 0F 11 46 10                  movups xmmword ptr [r14 + 0x10], xmm0
00B28048  41 0F 11 46 20                  movups xmmword ptr [r14 + 0x20], xmm0
00B2804D  E9 1F A2 E3 FF                  jmp 0x140962271
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B27F7C(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbx;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned __int8 v_stack_p80;
    unsigned __int64 v_stack_p98;

    if ((((unsigned __int8)(a1)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
    }
    a3 = ((unsigned int)(a2)) + (a1);
    if (a3 > result) goto loc_00B27FA0;
    if (a3 < a1) {
        result = *(unsigned __int8 *)(result);
        v_rbx = v_stack_p34;
    }
    if (a2 < 36) goto loc_00B27FF6;
    if ((*(unsigned int *)(a1)) != 36) goto loc_00B27FF6;
    *(unsigned int *)(a4) = 48;
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    *(unsigned int *)(a4 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)));
    *(unsigned __int64 *)(a4 + 16) = (unsigned int)(*(unsigned int *)(a1 + 12));
    *(unsigned int *)(a4 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    *(unsigned int *)(a4 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)));
    *(unsigned int *)(a4 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)));
    *(unsigned int *)(a4 + 36) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 28)));
    *(unsigned int *)(a4 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    goto loc_00B27FFC;
loc_00B27FF6:
    v_stack_p34 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))));
loc_00B27FFC:
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B27F7C(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    uint8_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint8_t v_stack_p80;
    uint64_t v_stack_p98;

    if ((((uint8_t)(Arg1)) & (3)) != 0) {
        result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
    }
    Arg3 = ((uint32_t)(Arg2)) + (Arg1);
    if (Arg3 > result) goto loc_00B27FA0;
    if (Arg3 < Arg1) {
        result = *(uint8_t *)(result);
        local_rbx = v_stack_p34;
    }
    if (Arg2 < 36) goto loc_00B27FF6;
    if ((*(uint32_t *)(Arg1)) != 36) goto loc_00B27FF6;
    *(uint32_t *)(Arg4) = 48;
    *(uint32_t *)(Arg4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x4)));
    *(uint32_t *)(Arg4 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x8)));
    *(uint64_t *)(Arg4 + 0x10) = (uint32_t)(*(uint32_t *)(Arg1 + 0xC));
    *(uint32_t *)(Arg4 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)));
    *(uint32_t *)(Arg4 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x14)));
    *(uint32_t *)(Arg4 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x18)));
    *(uint32_t *)(Arg4 + 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x1C)));
    *(uint32_t *)(Arg4 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x20)));
    goto loc_00B27FFC;
loc_00B27FF6:
    v_stack_p34 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))));
loc_00B27FFC:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B27F7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B27F7C[BB_00B27F7C]
  bb_00B27F81[BB_00B27F81]
  bb_00B27F86[BB_00B27F86]
  bb_00B27F9B[BB_00B27F9B]
  bb_00B27FA0[BB_00B27FA0]
  bb_00B27FA6[BB_00B27FA6]
  bb_00B27FB0[BB_00B27FB0]
  bb_00B27FB5[BB_00B27FB5]
  bb_00B27FF6[BB_00B27FF6]
  bb_00B27FFC[BB_00B27FFC]
  bb_00B28001[BB_00B28001]
  bb_00B2802C[BB_00B2802C]
  bb_00B28037[BB_00B28037]
  bb_00B2803C[BB_00B2803C]
  bb_00B27F7C -->|branch| bb_00B27F86
  bb_00B27F7C -->|fallthrough| bb_00B27F81
  bb_00B27F81 -->|flow| bb_00B27F86
  bb_00B27F86 -->|branch| bb_00B27FA0
  bb_00B27F86 -->|fallthrough| bb_00B27F9B
  bb_00B27F9B -->|branch| bb_00B27FA6
  bb_00B27F9B -->|fallthrough| bb_00B27FA0
  bb_00B27FA0 -->|flow| bb_00B27FA6
  bb_00B27FA6 -->|branch| bb_00B27FF6
  bb_00B27FA6 -->|fallthrough| bb_00B27FB0
  bb_00B27FB0 -->|branch| bb_00B27FF6
  bb_00B27FB0 -->|fallthrough| bb_00B27FB5
  bb_00B27FB5 -->|branch| bb_00B27FFC
  bb_00B27FF6 -->|flow| bb_00B27FFC
  bb_00B2802C -->|fallthrough| bb_00B28037
```
