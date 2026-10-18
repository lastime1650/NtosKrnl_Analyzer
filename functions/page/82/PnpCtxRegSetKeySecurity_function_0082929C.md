# PnpCtxRegSetKeySecurity

- RVA: `0x0082929C`–`0x008292B6` (길이 `26` bytes)
- VA: `0x000000014082929C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008292AB` → [RegRtlSetKeySecurity](../83/RegRtlSetKeySecurity_function_00832CDC.md) (function, `0x00832CDC`)

### Direct callers
- [PnpRegCopyKeySecurity](../72/PnpRegCopyKeySecurity_function_0072CAC8.md) at `0x0072CBAD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0082929C  48 83 EC 28                     sub rsp, 0x28
008292A0  41 8B C0                        mov eax, r8d
008292A3  48 8B CA                        mov rcx, rdx
008292A6  8B D0                           mov edx, eax
008292A8  4D 8B C1                        mov r8, r9
008292AB  E8 2C 9A 00 00                  call 0x140832cdc
008292B0  48 83 C4 28                     add rsp, 0x28
008292B4  C3                              ret
008292B5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpCtxRegSetKeySecurity(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = RegRtlSetKeySecurity(a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpCtxRegSetKeySecurity(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = RegRtlSetKeySecurity(Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4, Arg4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0082929C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0082929C[BB_0082929C]
  bb_008292B5[BB_008292B5]
```
