# MiUpdateSharedUserDataNumberOfPages

- RVA: `0x007FB160`–`0x007FB196` (길이 `54` bytes)
- VA: `0x00000001407FB160`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiPerformMemoryChange](../../text/67/MiPerformMemoryChange_function_006733A8.md) at `0x0067359C`
- [MiInitSystem](../../init/C5/MiInitSystem_function_00C5E6C0.md) at `0x00C5E98D`

### Static image references
- `0x007FB160` → RVA `0x00FC5008` (`ALMOSTRO`; read)
- `0x007FB167` → RVA `0x00E3D550` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007FB160  48 8B 05 A1 9E 7C 00            mov rax, qword ptr [rip + 0x7c9ea1]
007FB167  48 8B 0D E2 23 64 00            mov rcx, qword ptr [rip + 0x6423e2]
007FB16E  48 89 88 10 03 00 00            mov qword ptr [rax + 0x310], rcx
007FB175  B9 FF FF FF FF                  mov ecx, 0xffffffff
007FB17A  48 8B 05 CF 23 64 00            mov rax, qword ptr [rip + 0x6423cf]
007FB181  48 3B C1                        cmp rax, rcx
007FB184  0F 46 C8                        cmovbe ecx, eax
007FB187  48 8B 05 7A 9E 7C 00            mov rax, qword ptr [rip + 0x7c9e7a]
007FB18E  89 88 E8 02 00 00               mov dword ptr [rax + 0x2e8], ecx
007FB194  C3                              ret
007FB195  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUpdateSharedUserDataNumberOfPages(void)
{
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8167073) + 784) = *(unsigned __int64 *)(v_rip + 6562786);
    a1 = (unsigned int)(0xFFFFFFFFULL);
    if ((*(unsigned __int64 *)(v_rip + 6562767)) <= ((unsigned int)(0xFFFFFFFFULL))) { a1 = (unsigned int)(*(unsigned __int64 *)(v_rip + 6562767)); }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 8167034) + 744) = (unsigned int)(a1);
    return *(unsigned __int64 *)(v_rip + 8167034);
}
```

## 5. (Beta) C Style

```c
void MiUpdateSharedUserDataNumberOfPages(void)
{
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x7C9EA1) + 0x310) = *(uint64_t *)(v_rip + 0x6423E2);
    a1 = (uint32_t)(0xFFFFFFFFULL);
    if ((*(uint64_t *)(v_rip + 0x6423CF)) <= ((uint32_t)(0xFFFFFFFFULL))) { a1 = (uint32_t)(*(uint64_t *)(v_rip + 0x6423CF)); }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x7C9E7A) + 0x2E8) = (uint32_t)(a1);
    return *(uint64_t *)(v_rip + 0x7C9E7A);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007FB160&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007FB160[BB_007FB160]
  bb_007FB195[BB_007FB195]
```
