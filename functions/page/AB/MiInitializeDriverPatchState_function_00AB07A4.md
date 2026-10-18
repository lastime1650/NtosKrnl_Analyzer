# MiInitializeDriverPatchState

- RVA: `0x00AB07A4`–`0x00AB07EB` (길이 `71` bytes)
- VA: `0x0000000140AB07A4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `22`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AB07BE` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [MiLockPatchIatForDV](../../text/68/MiLockPatchIatForDV_function_00682050.md) at `0x006820D8`
- [MiReapplyImportOptimizationForDriverVerifier](../../text/68/MiReapplyImportOptimizationForDriverVerifier_function_00682268.md) at `0x006822CC`
- [MmWriteSystemImageTracepoint](../../text/68/MmWriteSystemImageTracepoint_function_00684150.md) at `0x006841D3`
- [MmReapplyBootPatchImports](../../init/C6/MmReapplyBootPatchImports_function_00C67768.md) at `0x00C677CE`
- [MmReapplyBootPatchImports](../../init/C6/MmReapplyBootPatchImports_function_00C67768.md) at `0x00C677DA`
- [MmReapplyBootPatchImports](../../init/C6/MmReapplyBootPatchImports_function_00C67768.md) at `0x00C67803`
- [MmReapplyBootPatchImports](../../init/C6/MmReapplyBootPatchImports_function_00C67768.md) at `0x00C6780F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AB07BE` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB07A4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00AB07A9  57                              push rdi
00AB07AA  48 83 EC 20                     sub rsp, 0x20
00AB07AE  48 8B D9                        mov rbx, rcx
00AB07B1  48 8B FA                        mov rdi, rdx
00AB07B4  48 8D 4A 08                     lea rcx, [rdx + 8]
00AB07B8  33 D2                           xor edx, edx
00AB07BA  44 8D 42 60                     lea r8d, [rdx + 0x60]
00AB07BE  E8 7D 64 C1 FF                  call 0x1406c6c40
00AB07C3  48 89 1F                        mov qword ptr [rdi], rbx
00AB07C6  B8 00 00 00 00                  mov eax, 0
00AB07CB  8B 4B 40                        mov ecx, dword ptr [rbx + 0x40]
00AB07CE  F7 C1 FF 0F 00 00               test ecx, 0xfff
00AB07D4  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00AB07D9  0F 95 C0                        setne al
00AB07DC  C1 E9 0C                        shr ecx, 0xc
00AB07DF  03 C1                           add eax, ecx
00AB07E1  89 47 18                        mov dword ptr [rdi + 0x18], eax
00AB07E4  48 83 C4 20                     add rsp, 0x20
00AB07E8  5F                              pop rdi
00AB07E9  C3                              ret
00AB07EA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitializeDriverPatchState(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a2 = 0;
    result = memset(a2 + 8, a2, a2 + 96, a4);
    *(unsigned __int64 *)(a2) = a1;
    result = ((((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 64)))) & (0xFFFULL)) != 0) ? 1 : 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 64))) >> (12));
    result = (unsigned int)((result) + ((unsigned int)(a1)));
    *(unsigned int *)(a2 + 24) = (unsigned int)(result);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiInitializeDriverPatchState(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    result = memset(Arg2 + 8, Arg2, Arg2 + 96, a4);
    *(void **)(arg2) = Arg1;
    result = ((((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x40)))) & (0xFFFULL)) != 0) ? 1 : 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x40))) >> (12));
    result = (uint32_t)((result) + ((uint32_t)(Arg1)));
    *(uint32_t *)(arg2 + 0x18) = (uint32_t)(result);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x18` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB07A4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB07A4[BB_00AB07A4]
  bb_00AB07EA[BB_00AB07EA]
```
