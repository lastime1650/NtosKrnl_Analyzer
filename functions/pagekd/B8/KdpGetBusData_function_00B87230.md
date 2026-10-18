# KdpGetBusData

- RVA: `0x00B87230`–`0x00B872F1` (길이 `193` bytes)
- VA: `0x0000000140B87230`
- 실행 섹션: `PAGEKD`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C3968`
- 디코드: `51`개 명령, `193/193` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00B872A9` → [KdpSysReadBusData](KdpSysReadBusData_function_00B88540.md) (function, `0x00B88540`)
- `0x00B872D4` → `kdcom.dll!KdSendPacket` (import, 간접 대상; import `kdcom.dll!KdSendPacket`)

### Direct callers
- [KdpSendWaitContinue](KdpSendWaitContinue_function_00B8A32C.md) at `0x00B8A5A7`

### Static image references
- `0x00B87244` → RVA `0x00E0AA48` (`.data`; read)
- `0x00B872B2` → RVA `0x00F475E0` (`.data`; read)
- `0x00B872D4` → RVA `0x001516C0` (`kdcom.dll!KdSendPacket (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B87230  48 8B C4                        mov rax, rsp
00B87233  48 89 58 08                     mov qword ptr [rax + 8], rbx
00B87237  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00B8723B  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00B8723F  57                              push rdi
00B87240  48 83 EC 50                     sub rsp, 0x50
00B87244  44 8B 05 FD 37 28 00            mov r8d, dword ptr [rip + 0x2837fd]
00B8724B  48 8B F2                        mov rsi, rdx
00B8724E  BA 38 00 00 00                  mov edx, 0x38
00B87253  0F 57 C0                        xorps xmm0, xmm0
00B87256  0F 11 40 E8                     movups xmmword ptr [rax - 0x18], xmm0
00B8725A  48 89 48 F0                     mov qword ptr [rax - 0x10], rcx
00B8725E  48 8B F9                        mov rdi, rcx
00B87261  8B 49 20                        mov ecx, dword ptr [rcx + 0x20]
00B87264  66 89 50 E8                     mov word ptr [rax - 0x18], dx
00B87268  41 8B C0                        mov eax, r8d
00B8726B  48 2B C2                        sub rax, rdx
00B8726E  48 3B C8                        cmp rcx, rax
00B87271  76 04                           jbe 0x140b87277
00B87273  41 8D 48 C8                     lea ecx, [r8 - 0x38]
00B87277  0F B7 5E 02                     movzx ebx, word ptr [rsi + 2]
00B8727B  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00B87280  44 8B 4F 1C                     mov r9d, dword ptr [rdi + 0x1c]
00B87284  3B CB                           cmp ecx, ebx
00B87286  44 8B 47 18                     mov r8d, dword ptr [rdi + 0x18]
00B8728A  8B 57 14                        mov edx, dword ptr [rdi + 0x14]
00B8728D  0F 46 D9                        cmovbe ebx, ecx
00B87290  8B 4F 10                        mov ecx, dword ptr [rdi + 0x10]
00B87293  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00B87298  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
00B8729C  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
00B872A0  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00B872A5  89 5C 24 70                     mov dword ptr [rsp + 0x70], ebx
00B872A9  E8 92 12 00 00                  call 0x140b88540
00B872AE  39 5C 24 70                     cmp dword ptr [rsp + 0x70], ebx
00B872B2  4C 8D 0D 27 03 3C 00            lea r9, [rip + 0x3c0327]
00B872B9  89 47 08                        mov dword ptr [rdi + 8], eax
00B872BC  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00B872C1  0F 42 5C 24 70                  cmovb ebx, dword ptr [rsp + 0x70]
00B872C6  4C 8B C6                        mov r8, rsi
00B872C9  89 5F 20                        mov dword ptr [rdi + 0x20], ebx
00B872CC  B9 02 00 00 00                  mov ecx, 2
00B872D1  66 89 1E                        mov word ptr [rsi], bx
00B872D4  48 FF 15 E5 A3 5C FF            call qword ptr [rip - 0xa35c1b]
00B872DB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00B872E0  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00B872E5  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
00B872EA  48 83 C4 50                     add rsp, 0x50
00B872EE  5F                              pop rdi
00B872EF  C3                              ret
00B872F0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KdpGetBusData(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (80);
    *(unsigned __int64 *)(v_rsp - 24) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 16) = a1;
    *(unsigned __int16 *)(v_rsp - 24) = 56;
    result = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 2635773))))) - (56);
    if (((unsigned int)(*(unsigned int *)(a1 + 32))) >= = result) {
        a1 = (unsigned int)(*(unsigned int *)(v_rip + 2635773)) - 56;
    }
    v_rbx = *(unsigned __int16 *)(a2 + 2);
    if (((unsigned int)(a1)) <= ((unsigned int)(*(unsigned __int16 *)(a2 + 2)))) { v_rbx = (unsigned int)(a1); }
    v_stack_m28 = v_stack_p18;
    v_stack_m30 = (unsigned int)(v_rbx);
    v_stack_m38 = *(unsigned __int64 *)(a2 + 8);
    v_stack_p18 = (unsigned int)(v_rbx);
    result = KdpSysReadBusData((unsigned int)(*(unsigned int *)(a1 + 16)), (unsigned int)(*(unsigned int *)(a1 + 20)), (unsigned int)(*(unsigned int *)(a1 + 24)), (unsigned int)(*(unsigned int *)(a1 + 28)));
    *(unsigned int *)(a1 + 8) = (unsigned int)(result);
    if (v_stack_p18 < ((unsigned int)(v_rbx))) { v_rbx = v_stack_p18; }
    *(unsigned int *)(a1 + 32) = (unsigned int)(v_rbx);
    *(unsigned __int16 *)(a2) = (unsigned __int16)(v_rbx);
    result = kdcom_dll_KdSendPacket(2, v_stack_m18, a2, v_rip + 3932967);
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KdpGetBusData(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (80);
    *(uint64_t *)(local_rsp - 0x18) = v_xmm0;
    *(void **)(local_rsp - 0x10) = Arg1;
    *(uint16_t *)(local_rsp - 0x18) = 56;
    result = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2837FD))))) - (56);
    if (((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >= = result) {
        Arg1 = (uint32_t)(*(uint32_t *)(v_rip + 0x2837FD)) - 56;
    }
    local_rbx = *(uint16_t *)(arg2 + 0x2);
    if (((uint32_t)(Arg1)) <= ((uint32_t)(*(uint16_t *)(arg2 + 0x2)))) { local_rbx = (uint32_t)(Arg1); }
    v_stack_m28 = v_stack_p18;
    v_stack_m30 = (uint32_t)(local_rbx);
    v_stack_m38 = *(uint64_t *)(arg2 + 0x8);
    v_stack_p18 = (uint32_t)(local_rbx);
    result = KdpSysReadBusData((uint32_t)(*(uint32_t *)(arg1 + 0x10)), (uint32_t)(*(uint32_t *)(arg1 + 0x14)), (uint32_t)(*(uint32_t *)(arg1 + 0x18)), (uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(result);
    if (v_stack_p18 < ((uint32_t)(local_rbx))) { local_rbx = v_stack_p18; }
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)(local_rbx);
    *(uint16_t *)(arg2) = (uint16_t)(local_rbx);
    result = kernel_indirect_call(2, v_stack_m18, Arg2, v_rip + 3932967);
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |
| `Arg2` | `+ 0x0` | `16` | `W` |
| `Arg2` | `+ 0x2` | `16` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagekd&rva=0x00B87230&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B87230[BB_00B87230]
  bb_00B87273[BB_00B87273]
  bb_00B87277[BB_00B87277]
  bb_00B872F0[BB_00B872F0]
  bb_00B87230 -->|branch| bb_00B87277
  bb_00B87230 -->|fallthrough| bb_00B87273
  bb_00B87273 -->|flow| bb_00B87277
```
