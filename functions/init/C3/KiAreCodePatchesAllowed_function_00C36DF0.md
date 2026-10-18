# KiAreCodePatchesAllowed

- RVA: `0x00C36DF0`–`0x00C36E0E` (길이 `30` bytes)
- VA: `0x0000000140C36DF0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00C36DF6` → [VslGetNestedPageProtectionFlags](../../text/2F/VslGetNestedPageProtectionFlags_function_002F2164.md) (function, `0x002F2164`)

### Direct callers
- [CcInitializeBcbProfiler](../BE/CcInitializeBcbProfiler_function_00BEF294.md) at `0x00BEF951`
- [KeCheckedKernelInitialize](../BE/KeCheckedKernelInitialize_function_00BEFA6C.md) at `0x00BEFA89`
- [sub_00BF16D0](../BF/Unknown_function_00BF16D0.md) at `0x00BF175F`
- [sub_00BF16D0](../BF/Unknown_function_00BF16D0.md) at `0x00BF5F8D`
- [VslConnectSwInterrupt](../C7/VslConnectSwInterrupt_function_00C75C70.md) at `0x00C75D87`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C36DF6` → [VslGetNestedPageProtectionFlags](../../text/2F/VslGetNestedPageProtectionFlags_function_002F2164.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C36DF0  48 83 EC 28                     sub rsp, 0x28
00C36DF4  33 C9                           xor ecx, ecx
00C36DF6  E8 69 B3 6B FF                  call 0x1402f2164
00C36DFB  A9 00 05 00 00                  test eax, 0x500
00C36E00  B8 00 00 00 00                  mov eax, 0
00C36E05  0F 95 C0                        setne al
00C36E08  48 83 C4 28                     add rsp, 0x28
00C36E0C  C3                              ret
00C36E0D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiAreCodePatchesAllowed(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = 0;
    result = VslGetNestedPageProtectionFlags(a1, a2, a3, a4);
    result = ((((unsigned int)(result)) & (0x500ULL)) != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiAreCodePatchesAllowed(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = 0;
    result = VslGetNestedPageProtectionFlags(Arg1, a2, a3, a4);
    result = ((((uint32_t)(result)) & (0x500ULL)) != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C36DF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C36DF0[BB_00C36DF0]
  bb_00C36E0D[BB_00C36E0D]
```
