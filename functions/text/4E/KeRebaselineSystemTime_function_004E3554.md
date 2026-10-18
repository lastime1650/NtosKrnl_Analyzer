# KeRebaselineSystemTime

- RVA: `0x004E3554`–`0x004E357B` (길이 `39` bytes)
- VA: `0x00000001404E3554`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004E355A` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)

### Direct callers
- [PopInvokeSystemStateHandler](../../pagelk/B7/PopInvokeSystemStateHandler_function_00B76A6C.md) at `0x00B7706F`

### Static image references
- `0x004E355F` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x004E356D` → RVA `0x00E668C0` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004E3554  48 83 EC 28                     sub rsp, 0x28
004E3558  33 C9                           xor ecx, ecx
004E355A  E8 81 B2 E9 FF                  call 0x14037e7e0
004E355F  48 8B 0D A2 1A AE 00            mov rcx, qword ptr [rip + 0xae1aa2]
004E3566  48 89 81 48 03 00 00            mov qword ptr [rcx + 0x348], rax
004E356D  48 83 25 4B 33 98 00 00         and qword ptr [rip + 0x98334b], 0
004E3575  48 83 C4 28                     add rsp, 0x28
004E3579  C3                              ret
004E357A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeRebaselineSystemTime(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11410082) + 840) = result;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeRebaselineSystemTime(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, a2, a3, a4);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0xAE1AA2) + 0x348) = result;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004E3554&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004E3554[BB_004E3554]
  bb_004E357A[BB_004E357A]
```
