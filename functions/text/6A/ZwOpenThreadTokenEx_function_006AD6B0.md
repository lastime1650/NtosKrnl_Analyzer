# ZwOpenThreadTokenEx

- RVA: `0x006AD6B0`–`0x006AD6CF` (길이 `31` bytes)
- VA: `0x00000001406AD6B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C00C4`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [DifZwOpenThreadTokenExWrapper](../64/DifZwOpenThreadTokenExWrapper_function_00644B50.md) at `0x00644C54`
- [RtlpIsAppContainer](../../page/78/RtlpIsAppContainer_function_0078F37C.md) at `0x0078F3F3`
- [BiOpenEffectiveToken](../../page/A3/BiOpenEffectiveToken_function_00A3D810.md) at `0x00A3D846`
- [BiOpenEffectiveToken](../../page/A3/BiOpenEffectiveToken_function_00A3D810.md) at `0x00A3D880`
- [RtlpOpenThreadToken](../../page/A7/RtlpOpenThreadToken_function_00A746F4.md) at `0x00A7471A`
- [RtlpOpenThreadToken](../../page/A7/RtlpOpenThreadToken_function_00A746F4.md) at `0x00A74743`
- [SysCtxOpenEffectiveToken](../../page/AC/SysCtxOpenEffectiveToken_function_00ACEED8.md) at `0x00ACEEF7`

### Static image references
- `0x006AD6BC` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD6C9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD6B0  48 8B C4                        mov rax, rsp
006AD6B3  FA                              cli
006AD6B4  48 83 EC 10                     sub rsp, 0x10
006AD6B8  50                              push rax
006AD6B9  9C                              pushfq
006AD6BA  6A 10                           push 0x10
006AD6BC  48 8D 05 9D 5D 00 00            lea rax, [rip + 0x5d9d]
006AD6C3  50                              push rax
006AD6C4  B8 2F 00 00 00                  mov eax, 0x2f
006AD6C9  E9 F2 72 01 00                  jmp 0x1406c49c0
006AD6CE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwOpenThreadTokenEx(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwOpenThreadTokenEx(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD6B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD6B0[BB_006AD6B0]
  bb_006AD6CE[BB_006AD6CE]
```
