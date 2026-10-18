# FsRtlInitializeDedupChange

- RVA: `0x00715E00`–`0x00715E2B` (길이 `43` bytes)
- VA: `0x0000000140715E00`
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
- `0x00715E20` → [ExInitializeResourceLite](../../text/41/ExInitializeResourceLite_function_0041F9A0.md) (function, `0x0041F9A0`)

### Direct callers
- [FsRtlInitSystem](../../init/C2/FsRtlInitSystem_function_00C28EEC.md) at `0x00C29003`

### Static image references
- `0x00715E04` → RVA `0x00F8EFA0` (`.data`; read)
- `0x00715E0B` → RVA `0x00F8EFB0` (`.data`; read)
- `0x00715E12` → RVA `0x00F8EFA8` (`.data`; write)
- `0x00715E19` → RVA `0x00F8EFA0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00715E20` → [ExInitializeResourceLite](../../text/41/ExInitializeResourceLite_function_0041F9A0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00715E00  48 83 EC 28                     sub rsp, 0x28
00715E04  48 8D 05 95 91 87 00            lea rax, [rip + 0x879195]
00715E0B  48 8D 0D 9E 91 87 00            lea rcx, [rip + 0x87919e]
00715E12  48 89 05 8F 91 87 00            mov qword ptr [rip + 0x87918f], rax
00715E19  48 89 05 80 91 87 00            mov qword ptr [rip + 0x879180], rax
00715E20  E8 7B 9B D0 FF                  call 0x14041f9a0
00715E25  48 83 C4 28                     add rsp, 0x28
00715E29  C3                              ret
00715E2A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlInitializeDedupChange(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned __int64 *)(v_rip + 8884623) = v_rip + 8884629;
    *(unsigned __int64 *)(v_rip + 8884608) = v_rip + 8884629;
    result = ExInitializeResourceLite(v_rip + 8884638, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void FsRtlInitializeDedupChange(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(uint64_t *)(v_rip + 0x87918F) = v_rip + 8884629;
    *(uint64_t *)(v_rip + 0x879180) = v_rip + 8884629;
    result = ExInitializeResourceLite(v_rip + 8884638, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00715E00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00715E00[BB_00715E00]
  bb_00715E2A[BB_00715E2A]
```
