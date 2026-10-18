# PiDevCfgSetDeviceRegProp

- RVA: `0x009635C0`–`0x00963604` (길이 `68` bytes)
- VA: `0x00000001409635C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `18`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009635F9` → [PiPnpRtlSetDeviceRegProperty](PiPnpRtlSetDeviceRegProperty_function_0096360C.md) (function, `0x0096360C`)

### Direct callers
- [PiDevCfgInitDeviceCallback](../73/PiDevCfgInitDeviceCallback_function_00733800.md) at `0x00733918`
- [PiDevCfgProcessDeviceCallback](../73/PiDevCfgProcessDeviceCallback_function_00734080.md) at `0x007341EC`
- [PiDevCfgProcessDeviceCallback](../73/PiDevCfgProcessDeviceCallback_function_00734080.md) at `0x00734227`
- [PpDevCfgProcessDeviceClass](../73/PpDevCfgProcessDeviceClass_function_00736824.md) at `0x00736BC0`
- [PpDevCfgProcessDeviceExtensions](../73/PpDevCfgProcessDeviceExtensions_function_00736C2C.md) at `0x0073730F`
- [PiDevCfgMigrateDevice](PiDevCfgMigrateDevice_function_00963E60.md) at `0x0096404B`
- [PpDevCfgProcessDeviceReset](PpDevCfgProcessDeviceReset_function_00965498.md) at `0x00965719`
- [sub_00B47D18](../B4/Unknown_function_00B47D18.md) at `0x00B47E02`

### Static image references
- `0x009635C6` → RVA `0x00E66398` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009635C0  48 83 EC 48                     sub rsp, 0x48
009635C4  8B 02                           mov eax, dword ptr [rdx]
009635C6  48 8B 0D CB 2D 50 00            mov rcx, qword ptr [rip + 0x502dcb]
009635CD  83 E0 01                        and eax, 1
009635D0  C1 E0 11                        shl eax, 0x11
009635D3  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
009635D7  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
009635DB  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009635DF  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
009635E4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009635E9  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
009635EE  45 8B C8                        mov r9d, r8d
009635F1  4C 8B 42 10                     mov r8, qword ptr [rdx + 0x10]
009635F5  48 8B 52 08                     mov rdx, qword ptr [rdx + 8]
009635F9  E8 0E 00 00 00                  call 0x14096360c
009635FE  48 83 C4 48                     add rsp, 0x48
00963602  C3                              ret
00963603  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgSetDeviceRegProp(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2))) & (1));
    result = (unsigned int)((result) << (17));
    v_stack_m10 = (unsigned int)(result);
    v_stack_m18 = (unsigned int)((unsigned int)(a6));
    v_stack_m20 = a5;
    v_stack_m28 = a4;
    result = PiPnpRtlSetDeviceRegProperty(*(unsigned __int64 *)(v_rip + 5254603), *(unsigned __int64 *)(a2 + 8), *(unsigned __int64 *)(a2 + 16), (unsigned int)(a3));
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgSetDeviceRegProp(int64_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, uint32_t Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2))) & (1));
    result = (uint32_t)((result) << (17));
    v_stack_m10 = (uint32_t)(result);
    v_stack_m18 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m20 = Arg5;
    v_stack_m28 = Arg4;
    result = PiPnpRtlSetDeviceRegProperty(*(uint64_t *)(v_rip + 0x502DCB), *(uint64_t *)(arg2 + 0x8), *(uint64_t *)(arg2 + 0x10), (uint32_t)(Arg3));
    local_rsp = (local_rsp) + (72);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009635C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009635C0[BB_009635C0]
  bb_00963603[BB_00963603]
```
