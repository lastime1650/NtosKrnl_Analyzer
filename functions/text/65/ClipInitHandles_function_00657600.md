# ClipInitHandles

- RVA: `0x00657600`–`0x0065765C` (길이 `92` bytes)
- VA: `0x0000000140657600`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `17`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x00657645` → `ext-ms-win-ntos-clipsp-l1-1-0.dll!ClipSpInitialize` (import, 간접 대상; import `ext-ms-win-ntos-clipsp-l1-1-0.dll!ClipSpInitialize`)
- `0x00657651` → [sub_00811D74](../../page/81/Unknown_function_00811D74.md) (function, `0x00811D74`)

### Direct callers
- [sub_009669C4](../../page/96/Unknown_function_009669C4.md) at `0x00966A1C`

### Static image references
- `0x00657604` → RVA `0x00AB3160` (`ExUpdateLicenseData`; read)
- `0x0065760D` → RVA `0x00FD8440` (`PAGEDATA`; write)
- `0x00657614` → RVA `0x00FD8320` (`PAGEDATA`; read)
- `0x0065761B` → RVA `0x0096BFF0` (`PAGE`; read)
- `0x00657622` → RVA `0x00FD8448` (`PAGEDATA`; write)
- `0x00657629` → RVA `0x007C7CA0` (`ExUpdateOsPfnInRegistry`; read)
- `0x00657630` → RVA `0x00FD8450` (`PAGEDATA`; write)
- `0x00657637` → RVA `0x00FD9AA0` (`PAGEDATA`; read)
- `0x0065763E` → RVA `0x00FD8458` (`PAGEDATA`; write)
- `0x00657645` → RVA `0x00151288` (`ext-ms-win-ntos-clipsp-l1-1-0.dll!ClipSpInitialize (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00657651` → [sub_00811D74](../../page/81/Unknown_function_00811D74.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00657600  48 83 EC 28                     sub rsp, 0x28
00657604  48 8D 05 55 BB 45 00            lea rax, [rip + 0x45bb55]
0065760B  33 C9                           xor ecx, ecx
0065760D  48 89 05 2C 0E 98 00            mov qword ptr [rip + 0x980e2c], rax
00657614  48 8D 15 05 0D 98 00            lea rdx, [rip + 0x980d05]
0065761B  48 8D 05 CE 49 31 00            lea rax, [rip + 0x3149ce]
00657622  48 89 05 1F 0E 98 00            mov qword ptr [rip + 0x980e1f], rax
00657629  48 8D 05 70 06 17 00            lea rax, [rip + 0x170670]
00657630  48 89 05 19 0E 98 00            mov qword ptr [rip + 0x980e19], rax
00657637  48 8B 05 62 24 98 00            mov rax, qword ptr [rip + 0x982462]
0065763E  48 89 05 13 0E 98 00            mov qword ptr [rip + 0x980e13], rax
00657645  48 FF 15 3C 9C AF FF            call qword ptr [rip - 0x5063c4]
0065764C  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00657651  E8 1E A7 1B 00                  call 0x140811d74
00657656  48 83 C4 28                     add rsp, 0x28
0065765A  C3                              ret
0065765B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ClipInitHandles(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = 0;
    *(unsigned __int64 *)(v_rip + 9965100) = v_rip + 4569941;
    *(unsigned __int64 *)(v_rip + 9965087) = v_rip + 3230158;
    *(unsigned __int64 *)(v_rip + 9965081) = v_rip + 1508976;
    *(unsigned __int64 *)(v_rip + 9965075) = *(unsigned __int64 *)(v_rip + 9970786);
    result = ext_ms_win_ntos_clipsp_l1_1_0_dll_ClipSpInitialize(a1, v_rip + 9964805, a3, a4);
    result = sub_00811D74(a1, v_rip + 9964805, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ClipInitHandles(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = 0;
    *(uint64_t *)(v_rip + 0x980E2C) = v_rip + 4569941;
    *(uint64_t *)(v_rip + 0x980E1F) = v_rip + 3230158;
    *(uint64_t *)(v_rip + 0x980E19) = v_rip + 1508976;
    *(uint64_t *)(v_rip + 0x980E13) = *(uint64_t *)(v_rip + 0x982462);
    result = kernel_indirect_call(Arg1, v_rip + 9964805, a3, a4);
    result = sub_00811D74(Arg1, v_rip + 9964805, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00657600&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00657600[BB_00657600]
  bb_0065765B[BB_0065765B]
```
