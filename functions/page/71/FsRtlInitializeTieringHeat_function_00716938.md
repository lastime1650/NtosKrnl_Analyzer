# FsRtlInitializeTieringHeat

- RVA: `0x00716938`–`0x00716963` (길이 `43` bytes)
- VA: `0x0000000140716938`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00716958` → [ExInitializeResourceLite](../../text/41/ExInitializeResourceLite_function_0041F9A0.md) (function, `0x0041F9A0`)

### Direct callers
- [FsRtlInitSystem](../../init/C2/FsRtlInitSystem_function_00C28EEC.md) at `0x00C28FFE`

### Static image references
- `0x0071693C` → RVA `0x00F8EF20` (`.data`; read)
- `0x00716943` → RVA `0x00F8EF30` (`.data`; read)
- `0x0071694A` → RVA `0x00F8EF28` (`.data`; write)
- `0x00716951` → RVA `0x00F8EF20` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00716958` → [ExInitializeResourceLite](../../text/41/ExInitializeResourceLite_function_0041F9A0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00716938  48 83 EC 28                     sub rsp, 0x28
0071693C  48 8D 05 DD 85 87 00            lea rax, [rip + 0x8785dd]
00716943  48 8D 0D E6 85 87 00            lea rcx, [rip + 0x8785e6]
0071694A  48 89 05 D7 85 87 00            mov qword ptr [rip + 0x8785d7], rax
00716951  48 89 05 C8 85 87 00            mov qword ptr [rip + 0x8785c8], rax
00716958  E8 43 90 D0 FF                  call 0x14041f9a0
0071695D  48 83 C4 28                     add rsp, 0x28
00716961  C3                              ret
00716962  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlInitializeTieringHeat(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned __int64 *)(v_rip + 8881623) = v_rip + 8881629;
    *(unsigned __int64 *)(v_rip + 8881608) = v_rip + 8881629;
    result = ExInitializeResourceLite(v_rip + 8881638, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void FsRtlInitializeTieringHeat(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(uint64_t *)(v_rip + 0x8785D7) = v_rip + 8881629;
    *(uint64_t *)(v_rip + 0x8785C8) = v_rip + 8881629;
    result = ExInitializeResourceLite(v_rip + 8881638, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00716938&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00716938[BB_00716938]
  bb_00716962[BB_00716962]
```
