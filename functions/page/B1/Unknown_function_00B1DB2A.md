# sub_00B1DB2A

- RVA: `0x00B1DB2A`–`0x00B1DB45` (길이 `27` bytes)
- VA: `0x0000000140B1DB2A`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00086F04`
- 디코드: `7`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00B1DB2C` → [_CmOpenDeviceRegKey + 0xB5](../8E/_CmOpenDeviceRegKey_function_008EE540.md) (`tail-transfer`)
  - `0x00B1DB37` → [_CmOpenDeviceRegKey + 0x108](../8E/_CmOpenDeviceRegKey_function_008EE540.md) (`tail-transfer`)
  - `0x00B1DB40` → [_CmOpenDeviceRegKey + 0xF3](../8E/_CmOpenDeviceRegKey_function_008EE540.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B1DB2A  85 C0                           test eax, eax
00B1DB2C  0F 84 C3 0A DD FF               je 0x1408ee5f5
00B1DB32  BF E5 00 00 C0                  mov edi, 0xc00000e5
00B1DB37  E9 0C 0B DD FF                  jmp 0x1408ee648
00B1DB3C  85 C9                           test ecx, ecx
00B1DB3E  75 F2                           jne 0x140b1db32
00B1DB40  E9 EE 0A DD FF                  jmp 0x1408ee633
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00B1DB2A(int a1)
{
loc_00B1DB32:
}
```

## 5. (Beta) C Style

```c
void sub_00B1DB2A(int32_t Arg1)
{
loc_00B1DB32:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B1DB2A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B1DB2A[BB_00B1DB2A]
  bb_00B1DB32[BB_00B1DB32]
  bb_00B1DB3C[BB_00B1DB3C]
  bb_00B1DB40[BB_00B1DB40]
  bb_00B1DB2A -->|fallthrough| bb_00B1DB32
  bb_00B1DB3C -->|branch| bb_00B1DB32
  bb_00B1DB3C -->|fallthrough| bb_00B1DB40
```
