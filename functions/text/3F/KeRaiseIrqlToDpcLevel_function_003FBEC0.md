# KeRaiseIrqlToDpcLevel

- RVA: `0x003FBEC0`–`0x003FBEF3` (길이 `51` bytes)
- VA: `0x00000001403FBEC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006AD84`
- 디코드: `16`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003FBEEC` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x003FBED3` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003FBEC0  40 53                           push rbx
003FBEC2  48 83 EC 20                     sub rsp, 0x20
003FBEC6  44 0F 20 C3                     mov rbx, cr8
003FBECA  B8 02 00 00 00                  mov eax, 2
003FBECF  44 0F 22 C0                     mov cr8, rax
003FBED3  83 3D 46 AE BC 00 00            cmp dword ptr [rip + 0xbcae46], 0
003FBEDA  75 0A                           jne 0x1403fbee6
003FBEDC  0F B6 C3                        movzx eax, bl
003FBEDF  48 83 C4 20                     add rsp, 0x20
003FBEE3  5B                              pop rbx
003FBEE4  C3                              ret
003FBEE5  CC                              int3
003FBEE6  0F B6 D0                        movzx edx, al
003FBEE9  0F B6 CB                        movzx ecx, bl
003FBEEC  E8 0B 98 0F 00                  call 0x1404f56fc
003FBEF1  EB E9                           jmp 0x1403fbedc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeRaiseIrqlToDpcLevel(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 12365382)) != 0) goto loc_003FBEE6;
loc_003FBEDC:
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_cr8);
loc_003FBEE6:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_cr8), (unsigned __int8)((unsigned __int8)(v_cr8)), a3, a4);
    goto loc_003FBEDC;
}
```

## 5. (Beta) C Style

```c
void KeRaiseIrqlToDpcLevel(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0xBCAE46)) != 0) goto loc_003FBEE6;
loc_003FBEDC:
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(v_cr8);
loc_003FBEE6:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_cr8), (uint8_t)((uint8_t)(v_cr8)), a3, a4);
    goto loc_003FBEDC;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003FBEC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003FBEC0[BB_003FBEC0]
  bb_003FBEDC[BB_003FBEDC]
  bb_003FBEE5[BB_003FBEE5]
  bb_003FBEE6[BB_003FBEE6]
  bb_003FBEC0 -->|branch| bb_003FBEE6
  bb_003FBEC0 -->|fallthrough| bb_003FBEDC
  bb_003FBEE5 -->|flow| bb_003FBEE6
  bb_003FBEE6 -->|branch| bb_003FBEDC
```
