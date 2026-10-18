# MmStrongCodeGuaranteesEnforced

- RVA: `0x00C6C980`–`0x00C6C990` (길이 `16` bytes)
- VA: `0x0000000140C6C980`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `5`개 명령, `16/16` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KeFreeInitializationCode](../BE/KeFreeInitializationCode_function_00BEFB10.md) at `0x00BEFB14`
- [sub_00BF16D0](../BF/Unknown_function_00BF16D0.md) at `0x00BF2382`
- [sub_00BF16D0](../BF/Unknown_function_00BF16D0.md) at `0x00C164C4`
- [sub_00C7EB3D](../C7/Unknown_function_00C7EB3D.md) at `0x00C7EC5D`

### Static image references
- `0x00C6C980` → RVA `0x00FC6A88` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C6C980  48 8B 05 01 A1 35 00            mov rax, qword ptr [rip + 0x35a101]
00C6C987  48 C1 E8 0F                     shr rax, 0xf
00C6C98B  83 E0 01                        and eax, 1
00C6C98E  C3                              ret
00C6C98F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmStrongCodeGuaranteesEnforced(void)
{
    __int64 result;

    result = (*(unsigned __int64 *)(v_rip + 3514625)) >> (15);
    result = (unsigned int)((result) & (1));
    return result;
}
```

## 5. (Beta) C Style

```c
void MmStrongCodeGuaranteesEnforced(void)
{
    int64_t result;

    result = (*(uint64_t *)(v_rip + 0x35A101)) >> (15);
    result = (uint32_t)((result) & (1));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C6C980&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C6C980[BB_00C6C980]
  bb_00C6C98F[BB_00C6C98F]
```
