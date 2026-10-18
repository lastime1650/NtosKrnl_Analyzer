# KdpSetBusData

- RVA: `0x00B88398`–`0x00B8841C` (길이 `132` bytes)
- VA: `0x0000000140B88398`
- 실행 섹션: `PAGEKD`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C9994`
- 디코드: `35`개 명령, `132/132` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00B883E7` → [KdpSysWriteBusData](KdpSysWriteBusData_function_00B885A8.md) (function, `0x00B885A8`)
- `0x00B88409` → `kdcom.dll!KdSendPacket` (import, 간접 대상; import `kdcom.dll!KdSendPacket`)

### Direct callers
- [KdpSendWaitContinue](KdpSendWaitContinue_function_00B8A32C.md) at `0x00B8A5B9`

### Static image references
- `0x00B883EF` → RVA `0x00F475E0` (`.data`; read)
- `0x00B88409` → RVA `0x001516C0` (`kdcom.dll!KdSendPacket (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B88398  4C 8B DC                        mov r11, rsp
00B8839B  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
00B8839F  53                              push rbx
00B883A0  48 83 EC 50                     sub rsp, 0x50
00B883A4  44 8B 49 1C                     mov r9d, dword ptr [rcx + 0x1c]
00B883A8  0F 57 C0                        xorps xmm0, xmm0
00B883AB  44 8B 41 18                     mov r8d, dword ptr [rcx + 0x18]
00B883AF  B8 38 00 00 00                  mov eax, 0x38
00B883B4  83 64 24 70 00                  and dword ptr [rsp + 0x70], 0
00B883B9  48 8B D9                        mov rbx, rcx
00B883BC  0F 11 44 24 40                  movups xmmword ptr [rsp + 0x40], xmm0
00B883C1  66 89 44 24 40                  mov word ptr [rsp + 0x40], ax
00B883C6  49 8D 43 18                     lea rax, [r11 + 0x18]
00B883CA  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00B883CE  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
00B883D1  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00B883D5  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
00B883D9  8B 51 14                        mov edx, dword ptr [rcx + 0x14]
00B883DC  49 89 4B F0                     mov qword ptr [r11 - 0x10], rcx
00B883E0  8B 49 10                        mov ecx, dword ptr [rcx + 0x10]
00B883E3  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
00B883E7  E8 BC 01 00 00                  call 0x140b885a8
00B883EC  89 43 08                        mov dword ptr [rbx + 8], eax
00B883EF  4C 8D 0D EA F1 3B 00            lea r9, [rip + 0x3bf1ea]
00B883F6  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00B883FA  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00B883FF  45 33 C0                        xor r8d, r8d
00B88402  89 43 20                        mov dword ptr [rbx + 0x20], eax
00B88405  41 8D 48 02                     lea ecx, [r8 + 2]
00B88409  48 FF 15 B0 92 5C FF            call qword ptr [rip - 0xa36d50]
00B88410  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00B88415  48 83 C4 50                     add rsp, 0x50
00B88419  5B                              pop rbx
00B8841A  C3                              ret
00B8841B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KdpSetBusData(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m30;
    unsigned int v_stack_p18;

    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (80);
    v_stack_m18 = v_xmm0;
    v_stack_m18 = 56;
    *(unsigned __int64 *)(v_rsp - 40) = v_rsp + 24;
    v_stack_m30 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    *(unsigned __int64 *)(v_rsp - 16) = a1;
    *(unsigned __int64 *)(v_rsp - 56) = *(unsigned __int64 *)(a2 + 8);
    result = KdpSysWriteBusData((unsigned int)(*(unsigned int *)(a1 + 16)), (unsigned int)(*(unsigned int *)(a1 + 20)), (unsigned int)(*(unsigned int *)(a1 + 24)), (unsigned int)(*(unsigned int *)(a1 + 28)));
    *(unsigned int *)(a1 + 8) = (unsigned int)(result);
    a3 = 0;
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p18));
    result = kdcom_dll_KdSendPacket(a3 + 2, v_stack_m18, a3, v_rip + 3928554);
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KdpSetBusData(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m30;
    uint32_t v_stack_p18;

    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (80);
    v_stack_m18 = v_xmm0;
    v_stack_m18 = 56;
    *(uint64_t *)(local_rsp - 0x28) = local_rsp + 24;
    v_stack_m30 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    *(void **)(local_rsp - 0x10) = Arg1;
    *(uint64_t *)(local_rsp - 0x38) = *(uint64_t *)(arg2 + 0x8);
    result = KdpSysWriteBusData((uint32_t)(*(uint32_t *)(arg1 + 0x10)), (uint32_t)(*(uint32_t *)(arg1 + 0x14)), (uint32_t)(*(uint32_t *)(arg1 + 0x18)), (uint32_t)(*(uint32_t *)(arg1 + 0x1C)));
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)(result);
    Arg3 = 0;
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p18));
    result = kernel_indirect_call(Arg3 + 2, v_stack_m18, Arg3, v_rip + 3928554);
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
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagekd&rva=0x00B88398&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B88398[BB_00B88398]
  bb_00B8841B[BB_00B8841B]
```
