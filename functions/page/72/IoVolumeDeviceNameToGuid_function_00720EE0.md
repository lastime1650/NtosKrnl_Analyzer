# IoVolumeDeviceNameToGuid

- RVA: `0x00720EE0`–`0x00720F60` (길이 `128` bytes)
- VA: `0x0000000140720EE0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00091FE0`
- 디코드: `38`개 명령, `128/128` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00720F08` → [IoVolumeDeviceNameToGuidPath](../95/IoVolumeDeviceNameToGuidPath_function_00952CC0.md) (function, `0x00952CC0`)
- `0x00720F3C` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x00720F48` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00720F48` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00720EE0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00720EE5  48 89 7C 24 10                  mov qword ptr [rsp + 0x10], rdi
00720EEA  55                              push rbp
00720EEB  48 8B EC                        mov rbp, rsp
00720EEE  48 83 EC 40                     sub rsp, 0x40
00720EF2  48 8B DA                        mov rbx, rdx
00720EF5  33 FF                           xor edi, edi
00720EF7  33 C0                           xor eax, eax
00720EF9  48 89 7D E0                     mov qword ptr [rbp - 0x20], rdi
00720EFD  48 8D 55 E0                     lea rdx, [rbp - 0x20]
00720F01  48 89 7D E8                     mov qword ptr [rbp - 0x18], rdi
00720F05  89 45 F4                        mov dword ptr [rbp - 0xc], eax
00720F08  E8 B3 1D 23 00                  call 0x140952cc0
00720F0D  85 C0                           test eax, eax
00720F0F  78 3E                           js 0x140720f4f
00720F11  0F B7 45 E0                     movzx eax, word ptr [rbp - 0x20]
00720F15  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00720F19  48 8B 7D E8                     mov rdi, qword ptr [rbp - 0x18]
00720F1D  66 83 E8 14                     sub ax, 0x14
00720F21  66 89 45 F0                     mov word ptr [rbp - 0x10], ax
00720F25  48 8B D3                        mov rdx, rbx
00720F28  0F B7 45 E2                     movzx eax, word ptr [rbp - 0x1e]
00720F2C  66 83 E8 14                     sub ax, 0x14
00720F30  66 89 45 F2                     mov word ptr [rbp - 0xe], ax
00720F34  48 8D 47 14                     lea rax, [rdi + 0x14]
00720F38  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00720F3C  E8 AF 0F 1D 00                  call 0x1408f1ef0
00720F41  33 D2                           xor edx, edx
00720F43  48 8B CF                        mov rcx, rdi
00720F46  8B D8                           mov ebx, eax
00720F48  E8 23 19 46 00                  call 0x140b82870
00720F4D  8B C3                           mov eax, ebx
00720F4F  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00720F54  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00720F59  48 83 C4 40                     add rsp, 0x40
00720F5D  5D                              pop rbp
00720F5E  C3                              ret
00720F5F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoVolumeDeviceNameToGuid(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned __int16 v_stack_m16;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int16 v_stack_m26;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rdi;
    v_rsp = (v_rsp) - (64);
    v_rdi = 0;
    result = 0;
    v_stack_m28 = 0;
    v_stack_m20 = 0;
    v_stack_m14 = 0;
    result = IoVolumeDeviceNameToGuidPath(a1, v_stack_m28, a3, a4);
    v_rbx = a2;
    if (!(sign_flag)) {
        result = v_stack_m28;
        a1 = v_stack_m18;
        v_rdi = v_stack_m20;
        result = (unsigned __int16)((result) - (20));
        v_stack_m18 = (unsigned __int16)(result);
        a2 = a2;
        result = v_stack_m26;
        result = (unsigned __int16)((result) - (20));
        v_stack_m16 = (unsigned __int16)(result);
        result = v_rdi + 20;
        v_stack_m10 = result;
        result = RtlGUIDFromString(a1, a2, a3, a4);
        a2 = 0;
        a1 = v_rdi;
        v_rbx = (unsigned int)(result);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
        result = (unsigned int)(v_rbx);
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoVolumeDeviceNameToGuid(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint16_t v_stack_m16;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint16_t v_stack_m26;
    uint64_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rdi;
    local_rsp = (local_rsp) - (64);
    local_rdi = 0;
    result = 0;
    v_stack_m28 = 0;
    v_stack_m20 = 0;
    v_stack_m14 = 0;
    result = IoVolumeDeviceNameToGuidPath(Arg1, v_stack_m28, a3, a4);
    local_rbx = Arg2;
    if (!(sign_flag)) {
        result = v_stack_m28;
        Arg1 = v_stack_m18;
        local_rdi = v_stack_m20;
        result = (uint16_t)((result) - (20));
        v_stack_m18 = (uint16_t)(result);
        Arg2 = Arg2;
        result = v_stack_m26;
        result = (uint16_t)((result) - (20));
        v_stack_m16 = (uint16_t)(result);
        result = local_rdi + 20;
        v_stack_m10 = result;
        result = RtlGUIDFromString(Arg1, Arg2, a3, a4);
        Arg2 = 0;
        Arg1 = local_rdi;
        local_rbx = (uint32_t)(result);
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
        result = (uint32_t)(local_rbx);
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00720EE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00720EE0[BB_00720EE0]
  bb_00720F11[BB_00720F11]
  bb_00720F4F[BB_00720F4F]
  bb_00720F5F[BB_00720F5F]
  bb_00720EE0 -->|branch| bb_00720F4F
  bb_00720EE0 -->|fallthrough| bb_00720F11
  bb_00720F11 -->|flow| bb_00720F4F
```
