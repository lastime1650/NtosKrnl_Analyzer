# CcNotifyWriteBehind

- RVA: `0x0057BA4C`–`0x0057BA6C` (길이 `32` bytes)
- VA: `0x000000014057BA4C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0057BA61` → [CcForEachPartition](../2F/CcForEachPartition_function_002F0828.md) (function, `0x002F0828`)

### Direct callers
- [MiShutdownSystem](../../pagelk/B7/MiShutdownSystem_function_00B73934.md) at `0x00B73969`
- [MmDuplicateMemory](../../pagelk/B7/MmDuplicateMemory_function_00B74158.md) at `0x00B741F0`

### Static image references
- `0x0057BA53` → RVA `0x0057BA80` (`CcNotifyWriteBehindHelper`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0057BA4C  48 83 EC 28                     sub rsp, 0x28
0057BA50  45 33 C9                        xor r9d, r9d
0057BA53  48 8D 0D 26 00 00 00            lea rcx, [rip + 0x26]
0057BA5A  45 33 C0                        xor r8d, r8d
0057BA5D  41 8D 51 02                     lea edx, [r9 + 2]
0057BA61  E8 C2 4D D7 FF                  call 0x1402f0828
0057BA66  48 83 C4 28                     add rsp, 0x28
0057BA6A  C3                              ret
0057BA6B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcNotifyWriteBehind(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a4 = 0;
    a3 = 0;
    result = CcForEachPartition(v_rip + 38, a4 + 2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcNotifyWriteBehind(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg4 = 0;
    Arg3 = 0;
    result = CcForEachPartition(v_rip + 38, Arg4 + 2, Arg3, Arg4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0057BA4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0057BA4C[BB_0057BA4C]
  bb_0057BA6B[BB_0057BA6B]
```
