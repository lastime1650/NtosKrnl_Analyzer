# ViIrpDatabaseReleaseLockShared

- RVA: `0x00617740`–`0x00617758` (길이 `24` bytes)
- VA: `0x0000000140617740`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0061774D` → [ExReleaseSpinLockShared](../2F/ExReleaseSpinLockShared_function_002F0EF0.md) (function, `0x002F0EF0`)

### Direct callers
- [VfIrpDatabaseCheckExFreePool](../../pagevrfy/BB/VfIrpDatabaseCheckExFreePool_function_00BB3E54.md) at `0x00BB3EB0`
- [VfIrpDatabaseEntryFindAndLock](../../pagevrfy/BB/VfIrpDatabaseEntryFindAndLock_function_00BB7074.md) at `0x00BB70EC`
- [sub_00BBC2B4](../../pagevrfy/BB/Unknown_function_00BBC2B4.md) at `0x00BBC2BE`

### Static image references
- `0x00617746` → RVA `0x00F04888` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00617740  48 83 EC 28                     sub rsp, 0x28
00617744  8A D1                           mov dl, cl
00617746  48 8D 0D 3B D1 8E 00            lea rcx, [rip + 0x8ed13b]
0061774D  E8 9E 97 CD FF                  call 0x1402f0ef0
00617752  48 83 C4 28                     add rsp, 0x28
00617756  C3                              ret
00617757  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViIrpDatabaseReleaseLockShared(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExReleaseSpinLockShared(v_rip + 9359675, a1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViIrpDatabaseReleaseLockShared(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExReleaseSpinLockShared(v_rip + 9359675, Arg1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00617740&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00617740[BB_00617740]
  bb_00617757[BB_00617757]
```
