# KdpNotSupported

- RVA: `0x00B874E4`–`0x00B8752C` (길이 `72` bytes)
- VA: `0x0000000140B874E4`
- 실행 섹션: `PAGEKD`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `17`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00B87518` → `kdcom.dll!KdSendPacket` (import, 간접 대상; import `kdcom.dll!KdSendPacket`)

### Direct callers
- [KdpSendWaitContinue](KdpSendWaitContinue_function_00B8A32C.md) at `0x00B8A600`

### Static image references
- `0x00B874F7` → RVA `0x00F475E0` (`.data`; read)
- `0x00B87518` → RVA `0x001516C0` (`kdcom.dll!KdSendPacket (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B874E4  48 83 EC 38                     sub rsp, 0x38
00B874E8  B8 38 00 00 00                  mov eax, 0x38
00B874ED  C7 41 08 01 00 00 C0            mov dword ptr [rcx + 8], 0xc0000001
00B874F4  0F 57 C0                        xorps xmm0, xmm0
00B874F7  4C 8D 0D E2 00 3C 00            lea r9, [rip + 0x3c00e2]
00B874FE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00B87503  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00B87508  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00B8750D  8D 48 CA                        lea ecx, [rax - 0x36]
00B87510  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
00B87515  45 33 C0                        xor r8d, r8d
00B87518  48 FF 15 A1 A1 5C FF            call qword ptr [rip - 0xa35e5f]
00B8751F  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00B87524  33 C0                           xor eax, eax
00B87526  48 83 C4 38                     add rsp, 0x38
00B8752A  C3                              ret
00B8752B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KdpNotSupported(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    *(unsigned int *)(a1 + 8) = 0xC0000001ULL;
    v_stack_m18 = v_xmm0;
    v_stack_m10 = a1;
    v_stack_m18 = 56;
    a3 = 0;
    result = kdcom_dll_KdSendPacket(56 - 54, v_stack_m18, a3, v_rip + 3932386);
    result = 0;
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KdpNotSupported(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    *(uint32_t *)(arg1 + 0x8) = 0xC0000001ULL;
    v_stack_m18 = v_xmm0;
    v_stack_m10 = Arg1;
    v_stack_m18 = 56;
    Arg3 = 0;
    result = kernel_indirect_call(56 - 54, v_stack_m18, Arg3, v_rip + 3932386);
    result = 0;
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagekd&rva=0x00B874E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B874E4[BB_00B874E4]
  bb_00B8752B[BB_00B8752B]
```
