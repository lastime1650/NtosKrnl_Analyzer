# PsDereferenceSession

- RVA: `0x00A1827C`–`0x00A182BE` (길이 `66` bytes)
- VA: `0x0000000140A1827C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005DAC8`
- 디코드: `16`개 명령, `66/66` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A182B7` → [PspDereferenceSessionFinal](../78/PspDereferenceSessionFinal_function_00788F5C.md) (function, `0x00788F5C`)

### Direct callers
- [PsSessionCreate](../70/PsSessionCreate_function_00700438.md) at `0x0070058C`
- [MmCleanProcessAddressSpace](MmCleanProcessAddressSpace_function_00A17EC0.md) at `0x00A180C5`
- [MiCleanEmbryonicProcess](MiCleanEmbryonicProcess_function_00A1816C.md) at `0x00A18211`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A1827C  40 53                           push rbx
00A1827E  48 83 EC 20                     sub rsp, 0x20
00A18282  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A1828B  48 8B 98 B8 00 00 00            mov rbx, qword ptr [rax + 0xb8]
00A18292  83 C8 FF                        or eax, 0xffffffff
00A18295  48 8B 8B E8 02 00 00            mov rcx, qword ptr [rbx + 0x2e8]
00A1829C  F0 0F C1 01                     lock xadd dword ptr [rcx], eax
00A182A0  83 F8 01                        cmp eax, 1
00A182A3  74 12                           je 0x140a182b7
00A182A5  F0 81 A3 F4 01 00 00 FF FF FE FF  lock and dword ptr [rbx + 0x1f4], 0xfffeffff
00A182B0  48 83 C4 20                     add rsp, 0x20
00A182B4  5B                              pop rbx
00A182B5  C3                              ret
00A182B6  CC                              int3
00A182B7  E8 A0 0C D7 FF                  call 0x140788f5c
00A182BC  EB E7                           jmp 0x140a182a5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsDereferenceSession(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (unsigned int)((*(unsigned __int64 *)(gs_base + (0 + 392))) | (0xFFFFFFFFULL));
    if (((unsigned int)(result)) == 1) goto loc_00A182B7;
loc_00A182A5:
    v_rsp = (v_rsp) + (32);
    return result;
loc_00A182B7:
    result = PspDereferenceSessionFinal(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 744), a2, a3, a4);
    goto loc_00A182A5;
}
```

## 5. (Beta) C Style

```c
void PsDereferenceSession(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (uint32_t)((*(uint64_t *)(gs_base + (0 + 0x188))) | (0xFFFFFFFFULL));
    if (((uint32_t)(result)) == 1) goto loc_00A182B7;
loc_00A182A5:
    local_rsp = (local_rsp) + (32);
    return result;
loc_00A182B7:
    result = PspDereferenceSessionFinal(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x2E8), a2, a3, a4);
    goto loc_00A182A5;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A1827C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A1827C[BB_00A1827C]
  bb_00A182A5[BB_00A182A5]
  bb_00A182B6[BB_00A182B6]
  bb_00A182B7[BB_00A182B7]
  bb_00A1827C -->|branch| bb_00A182B7
  bb_00A1827C -->|fallthrough| bb_00A182A5
  bb_00A182B6 -->|flow| bb_00A182B7
  bb_00A182B7 -->|branch| bb_00A182A5
```
