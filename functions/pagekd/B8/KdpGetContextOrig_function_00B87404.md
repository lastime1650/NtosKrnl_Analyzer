# KdpGetContextOrig

- RVA: `0x00B87404`–`0x00B87469` (길이 `101` bytes)
- VA: `0x0000000140B87404`
- 실행 섹션: `PAGEKD`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E5F8`
- 디코드: `25`개 명령, `101/101` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00B8742B` → [KdpGetContext](KdpGetContext_function_00B872F8.md) (function, `0x00B872F8`)
- `0x00B87451` → `kdcom.dll!KdSendPacket` (import, 간접 대상; import `kdcom.dll!KdSendPacket`)

### Direct callers
- [KdpSendWaitContinue](KdpSendWaitContinue_function_00B8A32C.md) at `0x00B8A4B4`

### Static image references
- `0x00B87436` → RVA `0x00F475D0` (`.data`; write)
- `0x00B8743D` → RVA `0x00F475E0` (`.data`; read)
- `0x00B87451` → RVA `0x001516C0` (`kdcom.dll!KdSendPacket (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B87404  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00B87409  57                              push rdi
00B8740A  48 83 EC 30                     sub rsp, 0x30
00B8740E  0F 57 C0                        xorps xmm0, xmm0
00B87411  B8 38 00 00 00                  mov eax, 0x38
00B87416  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00B8741B  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
00B87420  48 8B FA                        mov rdi, rdx
00B87423  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B87428  48 8B D9                        mov rbx, rcx
00B8742B  E8 C8 FE FF FF                  call 0x140b872f8
00B87430  83 7B 08 00                     cmp dword ptr [rbx + 8], 0
00B87434  75 07                           jne 0x140b8743d
00B87436  C6 05 93 01 3C 00 01            mov byte ptr [rip + 0x3c0193], 1
00B8743D  4C 8D 0D 9C 01 3C 00            lea r9, [rip + 0x3c019c]
00B87444  4C 8B C7                        mov r8, rdi
00B87447  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00B8744C  B9 02 00 00 00                  mov ecx, 2
00B87451  48 FF 15 68 A2 5C FF            call qword ptr [rip - 0xa35d98]
00B87458  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00B8745D  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00B87462  48 83 C4 30                     add rsp, 0x30
00B87466  5F                              pop rdi
00B87467  C3                              ret
00B87468  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KdpGetContextOrig(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    v_stack_m18 = v_xmm0;
    v_stack_m18 = 56;
    v_stack_m10 = a1;
    result = KdpGetContext(a1, a2, a3, a4);
    if ((*(unsigned int *)(a1 + 8)) == 0) {
        *(unsigned __int8 *)(v_rip + 3932563) = 1;
    }
    result = kdcom_dll_KdSendPacket(2, v_stack_m18, a2, v_rip + 3932572);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KdpGetContextOrig(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    v_stack_m18 = v_xmm0;
    v_stack_m18 = 56;
    v_stack_m10 = Arg1;
    result = KdpGetContext(Arg1, Arg2, a3, a4);
    if ((*(uint32_t *)(arg1 + 0x8)) == 0) {
        *(uint8_t *)(v_rip + 0x3C0193) = 1;
    }
    result = kernel_indirect_call(2, v_stack_m18, Arg2, v_rip + 3932572);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagekd&rva=0x00B87404&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B87404[BB_00B87404]
  bb_00B87436[BB_00B87436]
  bb_00B8743D[BB_00B8743D]
  bb_00B87468[BB_00B87468]
  bb_00B87404 -->|branch| bb_00B8743D
  bb_00B87404 -->|fallthrough| bb_00B87436
  bb_00B87436 -->|flow| bb_00B8743D
```
