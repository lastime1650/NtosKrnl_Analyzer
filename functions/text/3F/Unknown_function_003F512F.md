# sub_003F512F

- RVA: `0x003F512F`–`0x003F5144` (길이 `21` bytes)
- VA: `0x00000001403F512F`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097404`
- 디코드: `6`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003F5136` → [RtlpCopyLegacyContextX86](RtlpCopyLegacyContextX86_function_003F56E0.md) (function, `0x003F56E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003F513B` → [sub_003F4E8A + 0x25C](Unknown_function_003F4E8A.md) (`tail-transfer`)
  - `0x003F5142` → [sub_003F4E8A + 0x28B](Unknown_function_003F4E8A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003F512F  45 8B C2                        mov r8d, r10d
003F5132  40 0F B6 CD                     movzx ecx, bpl
003F5136  E8 A5 05 00 00                  call 0x1403f56e0
003F513B  EB A9                           jmp 0x1403f50e6
003F513D  B8 0D 00 00 C0                  mov eax, 0xc000000d
003F5142  EB D1                           jmp 0x1403f5115
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003F512F(void)
{
    __int64 result;

    result = RtlpCopyLegacyContextX86((unsigned __int8)(v_rbp), a2, (unsigned int)((unsigned int)(v_r10)), a4);
}
```

## 5. (Beta) C Style

```c
void sub_003F512F(void)
{
    int64_t result;

    result = RtlpCopyLegacyContextX86((uint8_t)(local_rbp), a2, (uint32_t)((uint32_t)(local_r10)), a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003F512F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003F512F[BB_003F512F]
  bb_003F513D[BB_003F513D]
```
