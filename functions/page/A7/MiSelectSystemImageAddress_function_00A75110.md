# MiSelectSystemImageAddress

- RVA: `0x00A75110`–`0x00A75147` (길이 `55` bytes)
- VA: `0x0000000140A75110`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005FA94`
- 디코드: `16`개 명령, `55/55` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A75116` → [MiReserveDriverPtes](MiReserveDriverPtes_function_00A75150.md) (function, `0x00A75150`)

### Direct callers
- [MiSelectImageBase](../98/MiSelectImageBase_function_009887B0.md) at `0x00988A74`
- [MiGetSystemAddressForImage](MiGetSystemAddressForImage_function_00A74EEC.md) at `0x00A75036`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A75110  48 83 EC 28                     sub rsp, 0x28
00A75114  33 D2                           xor edx, edx
00A75116  E8 35 00 00 00                  call 0x140a75150
00A7511B  48 8B C8                        mov rcx, rax
00A7511E  48 85 C0                        test rax, rax
00A75121  75 06                           jne 0x140a75129
00A75123  48 83 C4 28                     add rsp, 0x28
00A75127  C3                              ret
00A75128  CC                              int3
00A75129  48 C1 E1 19                     shl rcx, 0x19
00A7512D  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00A75137  48 C1 E0 19                     shl rax, 0x19
00A7513B  48 2B C8                        sub rcx, rax
00A7513E  48 C1 F9 10                     sar rcx, 0x10
00A75142  48 8B C1                        mov rax, rcx
00A75145  EB DC                           jmp 0x140a75123
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSelectSystemImageAddress(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = MiReserveDriverPtes(a1, a2, a3, a4);
    if (result != 0) goto loc_00A75129;
loc_00A75123:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A75129:
    a1 = (result) << (25);
    result = (result) << (25);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    goto loc_00A75123;
}
```

## 5. (Beta) C Style

```c
int64_t MiSelectSystemImageAddress(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = MiReserveDriverPtes(Arg1, Arg2, a3, a4);
    if (result != 0) goto loc_00A75129;
loc_00A75123:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A75129:
    Arg1 = (result) << (25);
    result = (result) << (25);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    goto loc_00A75123;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A75110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A75110[BB_00A75110]
  bb_00A75123[BB_00A75123]
  bb_00A75128[BB_00A75128]
  bb_00A75129[BB_00A75129]
  bb_00A75110 -->|branch| bb_00A75129
  bb_00A75110 -->|fallthrough| bb_00A75123
  bb_00A75128 -->|flow| bb_00A75129
  bb_00A75129 -->|branch| bb_00A75123
```
